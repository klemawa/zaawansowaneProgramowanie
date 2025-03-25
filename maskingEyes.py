import numpy as np
import cv2

# Wczytaj obraz w odcieniach szarości
image = cv2.imread('example2.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

# Wyświetlenie oryginalnego obrazu
cv2.imshow('Original', image)
cv2.waitKey(0)

# Tworzenie maski - elipsa na obszarze oczu
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.ellipse(mask, (image.shape[1] // 2, int(image.shape[0] * 0.35)),(100, 40), 0, 0, 360, 255, -1)

cv2.imshow("Elliptical Mask", mask)

# Nałożenie maski na obraz
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

cv2.destroyAllWindows()
