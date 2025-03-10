import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd, nie da się wczytać obrazu")
else:
    print("Obraz wczytany poprawnie")

cv2.imshow("Original", image)
cv2.waitKey(0)

image[500,760] = (0,0,255)
(b,g,r) = image[300,600]

cv2.imshow("Changed", image)
cv2.waitKey(0)

#(h, w) = image.shape[:2]
#(cX,cY) = (w // 2, h // 2)

#br = image[cY:h, cX:w]
#cv2.imshow("Bottom-Right Corner", br)
#cv2.waitKey(0)
