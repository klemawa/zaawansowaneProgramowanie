import numpy as np
import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()
cv2.imshow('Original', image)

#opencv
dark = cv2.subtract(np.uint8(image), np.uint8([80]))
cv2.imshow('Dark Image via OpenCV', dark)

#numpy
dark2 = np.uint8(image) - np.uint8([80])
cv2.imshow('Dark Image via NumPy', dark2)
cv2.waitKey(0)