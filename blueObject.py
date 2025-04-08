import cv2
import numpy as np

image = cv2.imread('exampleBlue.png')
if image is None:
    print("Nie można załadować obrazu. Sprawdź nazwę pliku i ścieżkę.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 100, 50])   # Dolna granica
upper_blue = np.array([140, 255, 255])  # Górna granica

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny", image)
cv2.imshow("Maska - niebieski", mask)
cv2.imshow("Wykryte obiekty - niebieski", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
