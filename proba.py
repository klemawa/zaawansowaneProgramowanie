import numpy as np
import cv2

image = cv2.imread('example.png')
cv2.imshow('Original', image)
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M) #jaśniejsze bo dodajemy macierze
cv2.imshow("Lighter", added)
subtracted = cv2.subtract(image, M) #ciemnijsze bo odejmujemy macierze
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()