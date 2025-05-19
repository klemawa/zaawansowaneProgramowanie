import cv2
import numpy as np

image = cv2.imread('regal.png')
image = cv2.resize(image, (700, 700))
template = cv2.imread('szablonRegal.png')
h, w = template.shape[:2]

res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.24
loc = np.where(res >= threshold)

for i in range(len(loc[0])):
    y = loc[0][i]
    x = loc[1][i]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Wynik', image)
cv2.waitKey(0)
cv2.destroyAllWindows()