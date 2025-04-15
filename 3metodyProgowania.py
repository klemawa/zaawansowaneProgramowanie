import cv2

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T100, thresh100) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
(T2, otsu) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU )

cv2.imshow("Orignalne", gray)
cv2.imshow("Progowanie T = 100", thresh100)
cv2.imshow("Obraz z progowaniem Otsu ", otsu)

#adaptacyjne  to progowanie na pojedynczych wycinkach
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 21)
gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,21)

cv2.imshow("Progowanie adaptacyjne MEAN", thresh)
cv2.imshow("Progowanie adaptacyjne GAUSSIAN", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()