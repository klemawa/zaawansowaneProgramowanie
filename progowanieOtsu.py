import cv2

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T1, original) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
(T2, otsu) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU )

cv2.imshow("Orignalne", original)
cv2.imshow("Obraz z progowaniem Otsu ", otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
