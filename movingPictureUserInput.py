import cv2
import numpy as np

print("Podaj wartość przesunięcia w prawo bądź lewo np.20/-20")
x = int(input())

print("Podaj wartość przesunięcia w górę bądź w dół np.20/-20")
y = int(input())

image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

M = np.float32([[1,0,x],[0,1,y]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Down', shifted)
cv2.waitKey(0)

