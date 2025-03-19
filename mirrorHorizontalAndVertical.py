import cv2

image = cv2.imread('example.png')

flipped = cv2.flip(image,1) # poziome 1, pionowi 0
flipped2 = cv2.flip(image,0) # poziome 1, pionowi 0

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.imshow('flipped horizontal', flipped)
cv2.imshow('flipped vertical', flipped2)

cv2.waitKey(0)