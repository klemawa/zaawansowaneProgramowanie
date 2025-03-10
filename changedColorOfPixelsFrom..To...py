import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd")
else:
    print("Git")
cv2.imshow('Orginal', image)
cv2.waitKey(0)

image[50:100,50:100] = (255,255,255)
cv2.imshow('Changed', image)
cv2.waitKey(0)