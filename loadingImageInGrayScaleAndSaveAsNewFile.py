import cv2
import os

image_gray = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)
if image_gray is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
filename = 'savedImage.png'

cv2.imwrite(filename, image_gray)

if filename is not None:
    print('Successfully saved')
else:
    print("Bląd")