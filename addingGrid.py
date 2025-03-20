import numpy as np
import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

height, width = image.shape
grid_height = height // 3
grid_width = width // 3

for i in range(3):
    for j in range(3):
        part = image[i*grid_height:(i+1)*grid_height, j*grid_width:(j+1)*grid_width]
        cv2.imshow(f'Part {i*3 + j + 1}', part)

cv2.waitKey(0)
cv2.destroyAllWindows()
