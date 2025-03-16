import cv2
import numpy as np

image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

#tutaj przesunięcie tyko teraz wartości ujemne bo lewo i góra
M = np.float32([[1,0,-20],[0,1,-50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('Shifted', shifted)
cv2.waitKey(0)