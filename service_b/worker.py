import pika
import time
import json
import os
import requests
import uuid  # <--- Do generowania unikalnych nazw dla plików z internetu
from ultralytics import YOLO

RABBIT_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
SERVICE_A_URL = os.environ.get('SERVICE_A_URL', 'http://service_a:5000/results')
IMAGES_DIR = '/app/images'
TEMP_DIR = '/tmp'

#model
print("Ładowanie modelu YOLO...", flush=True)
try:
    model = YOLO("../yolov8n.pt")
except Exception as e:
    print(f"Błąd modelu: {e}", flush=True)
    exit(1)


def callback(channel, method, properties, body):
    data = json.loads(body)
    #w json url to link albo zdjęcie
    input_source = data.get('url')

    print(f"Pobrano zadanie: {input_source}", flush=True)

    file_path_to_analyze = ""
    is_downloaded_temp_file = False  #czy trzeba usunąć

    #sprawdzamy czy link czy foto lokalne
    if input_source.startswith(('http://', 'https://')):
        try:
            print(f"Wykryto URL. Pobieranie...", flush=True)
            response = requests.get(input_source, timeout=10)
            if response.status_code == 200:
                #losowa nazwa w folderze /tmp
                temp_filename = f"{uuid.uuid4()}.jpg"
                file_path_to_analyze = os.path.join(TEMP_DIR, temp_filename)

                with open(file_path_to_analyze, 'wb') as f:
                    f.write(response.content)

                is_downloaded_temp_file = True
            else:
                print(f"Błąd pobierania pliku: Kod {response.status_code}", flush=True)
                channel.basic_ack(delivery_tag=method.delivery_tag)
                return
        except Exception as e:
            print(f"Błąd sieci przy pobieraniu: {e}",
            channel.basic_ack(delivery_tag=method.delivery_tag))
            return
    else:
        #plik lokalny w folderze images
        file_path_to_analyze = os.path.join(IMAGES_DIR, input_source)

    #analiza obrazu
    count = 0
    if os.path.exists(file_path_to_analyze):
        try:
            results = model(file_path_to_analyze, classes=[0], verbose=False)  # class 0 to 'person'
            count = len(results[0].boxes)
            print(f"Znaleziono: {count} osób.", flush=True)
        except Exception as e:
            print(f"Błąd analizy YOLO: {e}", flush=True)
            channel.basic_ack(delivery_tag=method.delivery_tag)
            #sprzątanie
            if is_downloaded_temp_file and os.path.exists(file_path_to_analyze):
                os.remove(file_path_to_analyze)
            return
    else:
        print(f"Brak pliku fizycznego: {file_path_to_analyze}. Wysyłam 0.", flush=True)

    #usuwanie pliku
    if is_downloaded_temp_file and os.path.exists(file_path_to_analyze):
        os.remove(file_path_to_analyze)
        print("Usunięto plik tymczasowy.", flush=True)

    #wysyłka do serwisu
    try:
        #wysyłamy url/nazwę pliku jako identyfikator
        payload = {"url": input_source, "person_count": count}
        response = requests.post(SERVICE_A_URL, json=payload, timeout=5)

        if response.status_code == 200:
            print("Zapisano w Serwisie A. ACK.", flush=True)
            channel.basic_ack(delivery_tag=method.delivery_tag)
        else:
            print(f"Serwis A zwrócił błąd {response.status_code}. NACK (requeue).", flush=True)
            time.sleep(2)
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    except requests.exceptions.RequestException as e:
        print(f"Serwis A nieosiągalny ({e}). NACK (requeue).", flush=True)
        time.sleep(5)
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


#pętla połączenia
while True:
    try:
        print(f"Łączenie z RabbitMQ na {RABBIT_HOST}...", flush=True)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
        channel = connection.channel()
        channel.queue_declare(queue='image_tasks', durable=True)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='image_tasks', on_message_callback=callback, auto_ack=False)

        print('Worker gotowy i oczekuje na wiadomości!', flush=True)
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError:
        print("RabbitMQ niedostępny, ponawiam za 5s...", flush=True)
        time.sleep(5)
    except Exception as e:
        print(f"Nieoczekiwany błąd workera: {e}", flush=True)
        time.sleep(5)