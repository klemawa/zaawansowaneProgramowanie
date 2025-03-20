import numpy as np
import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

startX = int(input("Podaj startX: "))
endX = int(input("Podaj endX: "))
startY = int(input("Podaj startY: "))
endY = int(input("Podaj endY: "))

roi = image[startY:endY, startX:endX]

cv2.imshow('ROI', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
