import os
import uuid
from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import HTMLResponse
import pika
import json
import cv2 as cv
import shutil
from pathlib import Path
from typing import Dict
import requests
import numpy as np
from io import BytesIO
import urllib.request

app = FastAPI()

#konfiguracja tego rabbita
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'detection_task_queue'

#sciezka do zpaisywanych plikow
UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(exist_ok=True)

cvNet = [cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt'), cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt'), cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt'), cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')]

def process_image(image_data: bytes, array_number: int):
    img = cv.imdecode(np.frombuffer(image_data, np.uint8), cv.IMREAD_COLOR)
    if img is None:
        raise HTTPException(status_code=400, detail="Unable to read the image.")

    rows, cols = img.shape[:2]
    cvNet[array_number].setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    cvOut = cvNet[array_number].forward()

    detected_people = 0
    for detection in cvOut[0, 0, :, :]:
        score = float(detection[2])
        if score > 0.3:  # Only certain detections
            detected_people += 1
            left = int(detection[3] * cols)
            top = int(detection[4] * rows)
            right = int(detection[5] * cols)
            bottom = int(detection[6] * rows)
            cv.rectangle(img, (left, top), (right, bottom), (23, 230, 210), thickness=2)

    return detected_people

@app.get("/from_hard_drive")
async def from_hard_drive():
    try:
        file_path = r"C:\Users\Klementyna\PycharmProjects\zaawansowaneProgramowanie\Files_to_load\image.jpg"
        #dodawanie do tego rabbita, tworzenie id
        task_id = str(uuid.uuid4())

        #połaćzenie do rabbita
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps({"task_id": task_id, "file_path": str(file_path), "is_url": False}),
        )
        connection.close()
        return {"message": "Image uploaded successfully.", "task_id": task_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        #zapis foto
        if not file.filename.endswith(('.jpg', '.jpeg', '.png')):
            raise HTTPException(status_code=400, detail="Invalid file format. Allowed: .jpg, .jpeg, .png")

        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        #id i do rabbita
        task_id = str(uuid.uuid4())

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps({"task_id": task_id, "file_path": str(file_path), "is_url": False}),
        )
        connection.close()
        return {"message": "Image uploaded successfully.", "task_id": task_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@app.post("/upload_url/")
async def upload_image_from_url(url: str):
    try:
        task_id = str(uuid.uuid4())

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps({"task_id": task_id, "file_path": url, "is_url": True}),
        )
        connection.close()
        return {"message": "Image uploaded successfully.", "task_id": task_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e.args)}")


@app.get("/status/{task_id}")
async def check_status(task_id: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    return {"task_id": task_id, "status": "In progress", "detected_people": None}


import threading

#ustawienia rabbita
def start_consuming(thread_array_number: int):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME)

        def process_task(ch, method, properties, body):
            try:
                task_data = json.loads(body)
                task_id = task_data["task_id"]
                if task_data.get("is_url"):
                    file_path = UPLOAD_DIR / (task_id + ".jpg")
                    response = urllib.request.urlretrieve(task_data["file_path"], file_path)
                    with open(file_path, 'rb') as file:
                        detected_people = process_image(file.read(), thread_array_number)
                    os.remove(file_path)
                else:
                    with open(task_data["file_path"], 'rb') as file:
                        detected_people = process_image(file.read(), thread_array_number)

                #tu status rabbiota w sensie zadania
                print(
                    f"Task {task_id} completed: {detected_people} people detected.")
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=QUEUE_NAME, on_message_callback=process_task, consumer_tag=f"Consumer {thread_array_number}")

        channel.start_consuming()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

def start_rabbitmq_consumer(number: int):
    thread = threading.Thread(target=start_consuming, args=(number,))
    thread.daemon = True
    thread.name = f"rabbitmq_consumer_{number}"
    thread.start()

@app.on_event("startup")
async def startup_event():
    for init_number in range(4):
        start_rabbitmq_consumer(init_number)

    if 0:
        for picture_number in range(1000):
            await upload_image_from_url("https://www.shutterstock.com/shutterstock/photos/237624157/display_1500/stock-photo-two-people-sitting-on-a-bench-using-mobile-phone-237624157.jpg")



