import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd")
else:
    print("Git")
cv2.imshow('Orginal', image)
cv2.waitKey(0)

(h,w) = image.shape[:2]
startX, endX = w//3,2*w//3
startY, endY = h//3,2*h//3

srodkowyFragment = image[startY:endY,startX:endX]

flipped = cv2.flip(srodkowyFragment,-1)

image[startY:endY, startX:endX] = flipped #wklejenie do zdj

cv2.imshow('Z odwróconym fragmentem', image)
cv2.waitKey(0)