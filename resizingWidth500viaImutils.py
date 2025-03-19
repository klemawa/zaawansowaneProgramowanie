import cv2
import imutils

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

print("Obraz załadowany prawidłowo")
cv2.imshow("Original", image)
cv2.waitKey(0)

resized = imutils.resize(image, width=500)
cv2.imshow("Resized", resized)
cv2.waitKey(0)

cv2.destroyAllWindows()