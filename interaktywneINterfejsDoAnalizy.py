import cv2
import numpy as np

img = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)

def update(val):
    block_size = cv2.getTrackbarPos('blockSize', 'Adaptive Threshold')
    C = cv2.getTrackbarPos('C', 'Adaptive Threshold') - 20

    if block_size % 2 == 0:
        block_size += 1
    if block_size < 3:
        block_size = 3

    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, block_size, C)
    cv2.imshow('Adaptive Threshold', thresh)

cv2.namedWindow('Adaptive Threshold')
cv2.createTrackbar('blockSize', 'Adaptive Threshold', 11, 51, update)
cv2.createTrackbar('C', 'Adaptive Threshold', 20, 40, update)  # suwak od 0 do 40 -> -20 do 20

update(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
