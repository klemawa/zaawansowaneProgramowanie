import numpy as np
import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

cv2.imshow('Original', image)

M = np.float32([[1,0,-20],[0,1,-20]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('Image ', shifted)
cv2.imwrite('example2.jpg', shifted)

detection = cv2.absdiff(image, shifted)

#lcizba różniących sie pixeli
pixels = np.count_nonzero(detection)
totalPixels = detection.size

# Obliczanie detekcji w procentach
detectionPercentage = (pixels / totalPixels) * 100

print(f"Detekcja w procentach: {detectionPercentage:.2f}%")
cv2.waitKey(0)
cv2.destroyAllWindows()