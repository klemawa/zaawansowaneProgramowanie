import numpy as np
import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()
cv2.imshow('Original', image)

#opencv
added = cv2.add(np.uint8(image), np.uint8([50]))
cv2.imshow('Lighter Image via OpenCV', added)

#numpy
added2 = np.uint8(image) + np.uint8([50])
cv2.imshow('Light Image via NumPy', added2)
cv2.waitKey(0)