import cv2
import numpy as np

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

lower_blue = np.array([100, 150, 50])  # Dolna granica dla niebieskiego
upper_blue = np.array([140, 255, 255]) # Górna granica dla niebieskiego
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

combined_mask = cv2.bitwise_or(mask_red1, mask_red2)
combined_mask = cv2.bitwise_or(combined_mask, mask_green)
combined_mask = cv2.bitwise_or(combined_mask, mask_blue)

result = cv2.bitwise_and(image, image, mask=combined_mask)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maski połączone", combined_mask)
cv2.imshow("Wynik po nałożeniu maski", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
