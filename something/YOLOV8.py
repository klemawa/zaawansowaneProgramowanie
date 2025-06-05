import time
from ultralytics import YOLO
import cv2
import easyocr
import os
import Levenshtein
import time

# Wczytanie modelu i OCR
model = YOLO('yolov8.pt')
reader = easyocr.Reader(['pl','en'], gpu=False)
folder = 'images/'

start_time = time.time()

correct = 0
total = 0

# Wczytanie prawdziwych etykiet
with open('../labels.txt', 'r') as f:
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

import re

def clean_plate_text(text):
    if not text:
        return ""
    # Usuwamy wszystko co nie jest literą lub cyfrą, zamieniamy np. podobne znaki (’, `, . itd.)
    text = text.upper()
    text = re.sub(r'[^A-Z0-9]', '', text)
    # Zamiana podobnych znaków
    replacements = {
        '5': 'S', '6': 'G', '8': 'B', '0': 'O', '1': 'I', '3': 'B', '9': 'G',
        'O': '0', 'I': '1', 'B': '8', 'G': '6', 'S': '5'
    }
    corrected = ''.join(replacements.get(c, c) for c in text)
    return corrected


def fuzzy_match(s1, s2, max_dist=4):
    dist = Levenshtein.distance(s1, s2)
    return dist <= max_dist

def auto_correct_plate(text):
    # Funkcja zamienia potencjalne literówki w odczycie
    if not text:
        return ""
    corrected = ''
    for i, c in enumerate(text):
        if i in [0, 1, 6]:  # te indeksy są bardziej literowe
            zamiana = {'5':'S', '6':'G', '8':'B', '0':'O', '1':'L', '3':'B', '9':'G'}
            corrected += zamiana.get(c, c)
        else:  # reszta bardziej cyfrowa
            zamiana = {'S':'5', 'L':'1', 'I':'1', 'B':'8', 'O':'0', 'G':'6'}
            corrected += zamiana.get(c, c)
    return corrected

def is_match(pred, true):
    # Prosta równość - można rozbudować o fuzzy matching
    return pred == true

def extract_plate_text(img):
    results = model(img, verbose=False)
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

results_per_plate = {}

for filename in files:
    filepath = os.path.join(folder, filename)
    img = cv2.imread(filepath)
    if img is None:
        print(f"Nie można wczytać pliku: {filename}")
        continue

    odczytany = extract_plate_text(img)
    prawdziwy = true_labels.get(filename, None)

    odczytany_czysty = clean_plate_text(odczytany)
    prawdziwy_czysty = clean_plate_text(prawdziwy)

    pred_variants = [odczytany_czysty, auto_correct_plate(odczytany_czysty)]
    true_variants = [prawdziwy_czysty, auto_correct_plate(prawdziwy_czysty)]

    status = 'BŁĄD'
    for pred in pred_variants:
        for true in true_variants:
            if fuzzy_match(pred, true):
                correct += 1
                status = 'OK'
                break
        if status == 'OK':
            break

    results_per_plate[filename] = {
        'odczytany': odczytany,
        'prawdziwy': prawdziwy,
        'zgodny': (status == 'OK')
    }

    print(f"Plik: {filename} | Odczytano: {odczytany} | Prawdziwy: {prawdziwy} | Status: {status}")

end_time = time.time()
total_time = end_time - start_time

dokladnosc = (correct / len(files)) * 100
sredni_czas = total_time / len(files)



def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    return round(grade * 2) / 2


print(f'\n--- Podsumowanie ---')
print(f'Dokładność ogólna: {dokladnosc:.2f}%')
print(f'Łączny czas przetworzenia {len(files)} zdjęć: {total_time:.2f}s')
print(f'Średni czas na zdjęcie: {sredni_czas:.2f}s\n')

final_grade = calculate_final_grade(dokladnosc, total_time)
print(f'Ocena końcowa: {final_grade}')