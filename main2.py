import cv2
import easyocr
import os
import csv
import re
import time
import xml.etree.ElementTree as ET

folderWithImages = r"C:\Users\Mentyn\PycharmProjects\zaawansowaneProgramowanie\images"
csvFile = 'wyniki.csv'
cascadePath = 'haarcascade_russian_plate_number.xml'
annotationsFile = 'annotations.xml'

#adnotacje z XML
tree = ET.parse(annotationsFile)
root = tree.getroot()

annotations = {}
for image in root.findall('image'):
    filename = image.get('name')
    box = image.find('box')
    if box is not None:
        plate_number = box.find("attribute[@name='plate number']").text.strip().upper()
        annotations[filename] = re.sub(r'[^A-Z0-9]', '', plate_number)

plateCascade = cv2.CascadeClassifier(cascadePath)
reader = easyocr.Reader(['pl'])

startTime = time.time()

processed = 0
correct = 0
totalTested = 0

with open(csvFile, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Plik', 'Etykieta', 'Odczytany tekst', 'Zgadza się?', 'Dokładność OCR'])

    for filename in sorted(os.listdir(folderWithImages), key=lambda x: int(re.sub(r'\D', '', x) or 0)):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        filepath = os.path.join(folderWithImages, filename)
        img = cv2.imread(filepath)
        if img is None:
            writer.writerow([filename, annotations.get(filename, ''), 'brak obrazu', 'NIE', '0.00'])
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plates = plateCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=2, minSize=(30, 10))

        bestMatch = None
        bestConfidence = 0.0

        for (x, y, w, h) in plates:
            plateImg = img[y:y+h, x:x+w]
            h_, w_, _ = plateImg.shape
            plateCropped = plateImg[int(h_*0.2):int(h_*0.8), int(w_*0.1):int(w_*0.9)]

            ocrResult = reader.readtext(plateCropped, detail=0, paragraph=False)
            for text in ocrResult:
                textClean = re.sub(r'[^A-Z0-9]', '', text.upper())
                if (
                    5 <= len(textClean) <= 8 and
                    textClean.isalnum() and
                    any(c.isalpha() for c in textClean) and
                    any(c.isdigit() for c in textClean)
                ):
                    estimatedConf = len(textClean) / 8
                    if estimatedConf > bestConfidence:
                        bestConfidence = estimatedConf
                        bestMatch = textClean

        expected = annotations.get(filename, '')
        if expected:
            totalTested += 1

        if bestMatch:
            matchStatus = 'TAK' if bestMatch == expected else 'NIE'
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
    print(f"Trafień (OCR == etykieta): {correct}/{totalTested}")
    print(f"Dokładność: {correct / totalTested:.2%}")
else:
    print("Brak zdjęć z etykietami do obliczenia dokładności.")
