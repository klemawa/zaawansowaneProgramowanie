import cv2
import numpy as np

image = cv2.imread('example.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
h_shifted = (h.astype(int) + 30) % 180  # Hue ma zakres 0–179
h_shifted = h_shifted.astype(np.uint8)

hsv_shifted = cv2.merge([h_shifted, s, v])
image_shifted = cv2.cvtColor(hsv_shifted, cv2.COLOR_HSV2BGR)

cv2.imshow("Orignal", image)
cv2.imshow("Increased S", image_shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()