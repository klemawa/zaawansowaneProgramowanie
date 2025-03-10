import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd")
else:
    print("Git")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey(0)

image[0:cY, 0:cX] = (255,0,0)
cv2.imshow("Changed", image)
cv2.waitKey(0)