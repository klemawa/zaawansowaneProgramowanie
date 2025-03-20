import numpy as np
import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

cv2.imshow('Original', image)

M = np.ones(image.shape, dtype="uint8") * np.array([10, -20, 5])  # Zmiana kolorów RGB
M = np.clip(M, -255, 255)  # Ograniczenie wartości do zakresu -255 do 255
M = M.astype(np.uint8)  # Przekształcenie do typu uint8
image2 = cv2.add(image, M)  # Dodanie przekształceń do obrazu

cv2.imshow('Image Filter', image2)
cv2.imwrite('example2.jpg', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
