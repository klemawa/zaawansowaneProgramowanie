import cv2
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #sciezka do tesseract

folderDoObrazowSciezka = r'C:\Users\Klementyna\Desktop\fotyNaZajecia' # zmienic na odpowiednią ścieżkę gdy chcemy czytać ze zdjęcia

obrazy = [f for f in os.listdir(folderDoObrazowSciezka) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

for obrazPlik in obrazy:
    obrazySciezka = os.path.join(folderDoObrazowSciezka, obrazPlik)
    print(f"Otwieram plik: {obrazySciezka}")

    obraz = cv2.imread(obrazySciezka)
    if obraz is None:
        print(f"Nie można wczytać obrazu: {obrazySciezka}")
        continue

    szaraSkala = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)

    temp_filename = "temp_image.jpg"
    cv2.imwrite(temp_filename, szaraSkala)

    try:
        tekst = pytesseract.image_to_string(Image.open(temp_filename), lang='pol')
        print(f"Odczytany tekst z {obrazPlik}:\n{tekst}\n")
    except Exception as e:
        print(f"Błąd podczas odczytywania tekstu z {obrazPlik}: {e}")


    os.remove(temp_filename)

print("Przetwarzanie zakończone!")
