import cv2
import imutils

image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

(h,w) = image.shape[:2]
(cX,cY) = (w // 2, h // 2)
degree = 15
for i in range(360):
    M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0)
    rotated = imutils.rotate(image, degree)
    degree += degree
    cv2.imshow('Rotated', rotated)
    cv2.waitKey(5)