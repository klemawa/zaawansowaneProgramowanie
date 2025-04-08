import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(T1, binaryBasic) = cv2.threshold(gray, 100,255,cv2.THRESH_BINARY)
(T2, otsu) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Oryginalne z progowaniem T=100", binaryBasic)
cv2.imshow("Obraz z progowaniem Otsu", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()

# programowanie z otsu lepiej radzi sobie
#z bardziej złożonymi obrazami, czyli tutaj
#a zwykle progrowanie radzi sobie lepiej gdy
# kontrast między obiektem a tłem jest wyraźny
