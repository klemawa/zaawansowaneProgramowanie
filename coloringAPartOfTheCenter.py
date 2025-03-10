import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd")
else:
    print("Git")
(h,w) = image.shape[:2]
(cX, cY) = (w//2,h//2)
print(f'Środek; ({cX}, {cY})')

star = (cX - 50, cY - 50)
end = (cX + 50, cY + 50)

cv2.rectangle(image, star, end, (0,255,0), 2) # ta 2 na końcu to kreska, -1 to całe zamalowane

cv2.imshow('Obraz z czerwonym kwadratem', image)
cv2.waitKey(0)