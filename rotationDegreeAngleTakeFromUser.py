import cv2

print("Podaj kąt rotacji obrazu wokół środka np. lewo 45/prawo -45")
degreeAngle = int(input())
image = cv2.imread('example.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

(h,w) = image.shape[:2]
(cX,cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), degreeAngle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
