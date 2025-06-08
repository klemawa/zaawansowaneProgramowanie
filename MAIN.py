from fast_alpr import ALPR
import time
import os
import xml.etree.ElementTree as ET

def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    return round(grade * 2) / 2

def load_annotations(xml_path):
    mapping = {}
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for image in root.findall("image"):
        name = image.get("name")
        box = image.find("box")
        if box is not None:
            attribute = box.find("attribute[@name='plate number']")
            if attribute is not None:
                mapping[name] = attribute.text.strip()
    return mapping

alpr = ALPR(
    detector_model="yolo-v9-t-384-license-plate-end2end",
    ocr_model="global-plates-mobile-vit-v2-model",
)

folder = "images"
annotation_file = "annotations.xml"
annotations = load_annotations(annotation_file)

files = [f for f in os.listdir(folder) if f.lower().endswith(".jpg")]
files = sorted(files)[:100]

correct = 0
total = 0

total_start = time.time()

for idx, filename in enumerate(files, 1):
    image_path = os.path.join(folder, filename)
    start = time.time()
    alpr_results = alpr.predict(image_path)
    end = time.time()
    difference = end - start

    gt_plate = annotations.get(filename, None)
    pred_plate = alpr_results[0].ocr.text.strip() if alpr_results and alpr_results[0].ocr.text else None

    print(f"Plik: {filename}, Czas: {difference:.2f}s")
    print(f"GT: {gt_plate}, Pred: {pred_plate}")

    if gt_plate and pred_plate and gt_plate.upper() == pred_plate.upper():
        correct += 1
    total += 1
    print("OK" if gt_plate and pred_plate and gt_plate.upper() == pred_plate.upper() else "BŁĄD")
    print("-" * 40)

total_end = time.time()
total_difference = total_end - total_start

accuracy_percent = (correct / total) * 100 if total else 0
grade = calculate_final_grade(accuracy_percent, total_difference)

print(f"\nCałkowity czas przetwarzania {total} zdjęć: {total_difference:.2f}s")
print(f"Poprawnie rozpoznanych tablic: {correct} / {total} ({accuracy_percent:.2f}%)")
print(f"Ocena końcowa: {grade:.1f}")
