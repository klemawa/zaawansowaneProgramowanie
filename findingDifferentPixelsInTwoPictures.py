import numpy as np
import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

cv2.imshow('Original', image)

M = np.float32([[1,0,-20],[0,1,-20]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('Image ', shifted)
cv2.imwrite('example2.jpg', shifted)

bitwiseXor = cv2.bitwise_xor(image, shifted)
cv2.imshow('XOR', bitwiseXor)

cv2.waitKey(0)