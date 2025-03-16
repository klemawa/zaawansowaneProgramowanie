import cv2
import argparse
import imutils

image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)


M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (0,0))
cv2.imshow('Rotated by Left Corner', rotated)
cv2.waitKey(0)
