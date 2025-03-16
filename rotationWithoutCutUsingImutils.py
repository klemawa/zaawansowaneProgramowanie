import cv2
import imutils

image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

(h,w) = image.shape[:2]
(cX,cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = imutils.rotate_bound(image-75)
image = cv2.imwrite('rotated_output.png', rotated)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
