import time
from ultralytics import YOLO
import cv2
import easyocr
import os
import re
import numpy as np

model = YOLO('../license_plate_detector.pt')
reader = easyocr.Reader(['pl','en'], gpu=False)
folder = 'images/'

with open('labels.txt', 'r') as f:
    lines = f.read().strip().split('\n')
true_labels = {line.split()[0]: line.split()[1].upper() for line in lines}

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    gray = cv2.medianBlur(gray, 3)
    return gray

def popraw_tekst_z_regulami(tekst):
    tekst = tekst.upper()
    poprawiony = ''
    for i, c in enumerate(tekst):
        if i in [0, 1, 6]:
            zamiana = {'5':'S', '6':'G', '8':'B', '0':'O', '1':'L', '3':'B', '9':'G'}
            poprawiony += zamiana.get(c, c)
        else:
            zamiana = {'S':'5', 'L':'1', 'I':'1', 'B':'8', 'O':'0', 'G':'6'}
            poprawiony += zamiana.get(c, c)
    return poprawiony


def clean_text(text):
    if not text:
        return ""
    text = text.upper()
    return re.sub(r'[^A-Z0-9]', '', text)

def extract_plate_text(img):
    results = model(img)
    best_text = None
    best_conf = 0

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            plate = img[y1:y2, x1:x2]
            if plate.size == 0:
                continue
            scale = 200 / plate.shape[1]
            new_h = int(plate.shape[0] * scale)
            plate = cv2.resize(plate, (200, new_h))
            plate_processed = preprocess_image(plate)
            ocr_results = reader.readtext(plate_processed)
            for bbox, text, conf in ocr_results:
                if conf > best_conf and 5 <= len(text) <= 8:
                    best_conf = conf
                    best_text = popraw_tekst_z_regulami(text)
    return best_text

files = sorted(os.listdir(folder))[:100]

correct = 0
start_time = time.time()

# Słownik na wyniki dla każdej tablicy (plik)
results_per_plate = {}

for filename in files:
    filepath = os.path.join(folder, filename)
    img = cv2.imread(filepath)
    if img is None:
        print(f"Nie można wczytać pliku: {filename}")
        continue
    odczytany = extract_plate_text(img)
    prawdziwy = true_labels.get(filename, None)

    odczytany_czysty = clean_text(odczytany)
    prawdziwy_czysty = clean_text(prawdziwy)

    if prawdziwy and odczytany:
        is_correct = (odczytany_czysty == prawdziwy_czysty)
        if is_correct:
            correct += 1
    results_per_plate[filename] = {
        'odczytany': odczytany,
        'prawdziwy': prawdziwy,
        'zgodny': is_correct
    }
    print(f"Plik: {filename} | Odczytano: {odczytany} | Prawdziwy: {prawdziwy} | Zgadza się: {is_correct}")

end_time = time.time()
total_time = end_time - start_time

dokladnosc = correct / len(files) * 100
sredni_czas = total_time / len(files)

print(f'\n--- Podsumowanie ---')
print(f'Dokładność ogólna: {dokladnosc:.2f}%')
print(f'Łączny czas przetworzenia {len(files)} zdjęć: {total_time:.2f}s')
print(f'Średni czas na zdjęcie: {sredni_czas:.2f}s\n')

print('Dokładność per plik:')
for filename, res in results_per_plate.items():
    status = 'OK' if res['zgodny'] else 'BŁĄD'
    print(f"{filename}: Odczytano: {res['odczytany']}, Prawdziwy: {res['prawdziwy']}, Status: {status}")
