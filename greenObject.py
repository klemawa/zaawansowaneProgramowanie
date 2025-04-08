import cv2
import numpy as np

image = cv2.imread('exampleGreen.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 50, 50])  # Dolna granica zielonego
upper_green = np.array([85, 255, 255])  # Górna granica zielonego

mask = cv2.inRange(hsv, lower_green, upper_green)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maska zielonych obiektów", mask)
cv2.imshow("Wykryte zielone obiekty", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
