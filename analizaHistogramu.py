import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

(T1, original) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
(T2, otsu) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Oryginalne z progowaniem T=100", original)
cv2.imshow("Obraz z progowaniem Otsu", otsu)

plt.plot(hist)
plt.axvline(x=T2, color='r', linestyle='--')  # Zaznaczenie progu Otsu
plt.title("Histogram obrazu")
plt.xlabel("Intensywność")
plt.ylabel("Częstotliwość")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
