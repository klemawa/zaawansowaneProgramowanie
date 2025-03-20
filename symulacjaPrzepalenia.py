import numpy as np
import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()
cv2.imshow('Original', image)

#numpy
numpy = np.uint8(image) + np.uint8([150])
cv2.imshow('Overexposed via NumPy', numpy)

#opencv
opencv = cv2.add(np.uint8(image), np.uint8([150]))
cv2.imshow('Overexposed via OpenCV', opencv)

cv2.waitKey(0)
cv2.destroyAllWindows()