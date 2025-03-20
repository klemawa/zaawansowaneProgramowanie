import numpy as np
import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

width = image.shape[1]
halfWidth = width // 2

rightHalf = image[:, halfWidth:]

cv2.imshow('Right Half', rightHalf)

cv2.waitKey(0)
cv2.destroyAllWindows()
