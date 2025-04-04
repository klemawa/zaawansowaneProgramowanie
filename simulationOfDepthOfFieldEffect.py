import numpy as np
import cv2

image = cv2.imread('example6.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (21, 21), 0)

# Automatyczna segmentacja przez próg Otsu
_, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Inwersja maski (obiekt biały, tło czarne)
mask = cv2.bitwise_not(mask)

# Utworzenie efektu głębi ostrości
background = cv2.bitwise_and(blurred, blurred, mask=mask)
foreground = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
result = cv2.add(background, foreground)

# Wyświetlenie wyników
cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Rozmyte tło", result)
cv2.waitKey(0)
cv2.destroyAllWindows()