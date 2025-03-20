import numpy as np
import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()
roi = image[0:100, 0:100]

cv2.imshow('Original Image', image)
cv2.imshow('ROI', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()