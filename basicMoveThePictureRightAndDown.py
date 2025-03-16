import cv2
import numpy as np

image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

#tutaj przesunięcie
M = np.float32([[1,0,40],[0,1,40]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('Shifted', shifted)
cv2.waitKey(0)
