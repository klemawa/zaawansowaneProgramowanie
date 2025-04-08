import cv2
import numpy as np

image = cv2.imread('example2.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_skin = np.array([0, 30, 60])   # Dolna granica dla skóry
upper_skin = np.array([50, 150, 255])  # Górna granica dla skóry

mask = cv2.inRange(hsv, lower_skin, upper_skin)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maska skóry", mask)
cv2.imshow("Wykryte obszary skóry", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
