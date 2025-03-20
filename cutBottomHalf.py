import numpy as np
import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

#dwie równe części
height = image.shape[0]
halfHeight = height // 2

# Przycięcie dolnej połowy obrazu
bottom = image[halfHeight:, :]

# Wyświetlenie tylko dolnej połowy
cv2.imshow('Bottom Half', bottom)

cv2.waitKey(0)
cv2.destroyAllWindows()
