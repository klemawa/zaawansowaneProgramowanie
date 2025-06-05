import cv2
import easyocr
import os
import csv
import re
import time
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

folderWithImages = r"C:\\Users\\Klementyna\\PycharmProjects\\zaawansowaneProgramowanie\\images"
csvFile = 'wyniki.csv'
cascadePath = 'haarcascade_russian_plate_number.xml'
annotationsFile = 'annotations.xml'

def clean_text(text):
    return re.sub(r'[^A-Z0-9]', '', text.upper())

# Zamiana podobnych liter i liczb
def normalize(text):
    return text.replace('0', 'O').replace('1', 'I').replace('5', 'S')

# Metoda fuzzy porównanie z dopuszczeniem błędu
def is_match(predicted, actual, max_distance=1):
    pred_norm = normalize(predicted)
    act_norm = normalize(actual)
    ratio = SequenceMatcher(None, pred_norm, act_norm).ratio()
    return ratio >= 0.85

# Wczytanie adnotacji z XML
annotations = {}
root = ET.parse(annotationsFile).getroot()
for image in root.findall('image'):
    filename = image.get('name')
    box = image.find('box')
    if box is not None:
        plate_number = box.find("attribute[@name='plate number']").text.strip().upper()
        annotations[filename] = clean_text(plate_number)

plateCascade = cv2.CascadeClassifier(cascadePath)
reader = easyocr.Reader(['pl'], gpu=True)

startTime = time.time()
processed = 0
correct = 0
totalTested = 0

with open(csvFile, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Plik', 'Etykieta', 'Odczytany tekst', 'Zgadza się?', 'OCR trafność'])

    for filename in sorted(os.listdir(folderWithImages), key=lambda x: int(re.sub(r'\D', '', x) or 0)):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        filepath = os.path.join(folderWithImages, filename)
        img = cv2.imread(filepath)
        if img is None:
            writer.writerow([filename, annotations.get(filename, ''), 'brak obrazu', 'NIE', '0.00'])
            continue

        # Mniejsza rozdzielczość dla szybszego przetwarzania
        img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detekcja tablic - zmienione parametry dla lepszego wykrywania
        plates = plateCascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=3,
            minSize=(60, 15)
        )

        bestMatch = None
        bestConfidence = 0.0

        if len(plates) > 0:
            # Sprawdzenie wszystkich wykrytych tablic
            for (x, y, w, h) in plates:
                plateImg = img[y:y + h, x:x + w]
                # Mniej agresywne wycinanie tablicy
                cropped = plateImg[int(h * 0.05):int(h * 0.95), int(w * 0.05):int(w * 0.95)]

                ocrResult = reader.readtext(cropped, detail=0, paragraph=False)

                for text in ocrResult:
                    cleaned = clean_text(text)
                    if 6 <= len(cleaned) <= 8 and any(c.isalpha() for c in cleaned) and any(c.isdigit() for c in cleaned):
                        confidence = len(cleaned) / 8
                        if confidence > bestConfidence:
                            bestMatch = cleaned
                            bestConfidence = confidence

        expected = annotations.get(filename, '')
        if expected:
            totalTested += 1

        if bestMatch:
            matchStatus = 'TAK' if is_match(bestMatch, expected) else 'NIE'
            if matchStatus == 'TAK':
                correct += 1
            writer.writerow([filename, expected, bestMatch, matchStatus, f"{bestConfidence:.2f}"])
        else:
            writer.writerow([filename, expected, 'brak OCR', 'NIE', '0.00'])

        processed += 1

endTime = time.time()

print(f"\nWyniki dla wszystkich zdjęć w folderze:")
print(f"Łącznie przetworzono: {processed} zdjęć")
print(f"Czas przetwarzania: {endTime - startTime:.2f} s")
if totalTested > 0:
    accuracy_percent = (correct / totalTested) * 100
    print(f"Trafień (OCR ≈ etykieta): {correct}/{totalTested}")
    print(f"Dokładność: {accuracy_percent:.2f}%")

    # Przewidywany czas przetworzenia 100 zdjęć na podstawie obecnego tempa
    avg_time_per_image = (endTime - startTime) / processed
    predicted_100_time = avg_time_per_image * 100
    print(f"Przewidywany czas przetworzenia 100 zdjęć: {predicted_100_time:.2f} s")

    # Funkcja oceny (wg ustalonego wzoru)
    def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
        if accuracy_percent < 60 or processing_time_sec > 60:
            return 2.0
        accuracy_norm = (accuracy_percent - 60) / 40
        time_norm = (60 - processing_time_sec) / 50
        score = 0.7 * accuracy_norm + 0.3 * time_norm
        grade = 2.0 + 3.0 * score
        return round(grade * 2) / 2

    final_grade = calculate_final_grade(accuracy_percent, predicted_100_time)
    print(f"Końcowa ocena: {final_grade}")
else:
    print("Brak zdjęć z etykietami do obliczenia dokładności.")
