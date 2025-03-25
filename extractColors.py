import cv2
import numpy as np

# Wczytanie kolorowego obrazu
image = cv2.imread('flowers.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

# Konwersja do przestrzeni barw HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Zakres koloru czerwonego (dostosuj według potrzeby)
lower_purple = np.array([120, 50, 50])    # Dolna granica koloru
upper_purple = np.array([160, 255, 255])   # Górna granica koloru

# Tworzenie maski na podstawie zakresu koloru
mask = cv2.inRange(hsv, lower_purple, upper_purple)

# Uzyskanie obrazu z nałożoną maską
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Wyświetlenie wyników
cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maska koloru czerwonego", mask)
cv2.imshow("Ekstrakcja koloru czerwonego", masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
