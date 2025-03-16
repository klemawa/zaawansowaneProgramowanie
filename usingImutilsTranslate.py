import cv2
import imutils

image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

shifted = imutils.translate(image,0, 100)
cv2.imshow('Shifted Down', shifted)
cv2.waitKey(0)