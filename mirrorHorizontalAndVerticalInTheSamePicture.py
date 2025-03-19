import cv2

image = cv2.imread('example.png')

flipped = cv2.flip(image,-1) #i tak i tak względem obus osi

cv2.imshow('image', image)
cv2.waitKey(0)

cv2.imshow('flipped horizontal', flipped)
cv2.waitKey(0)