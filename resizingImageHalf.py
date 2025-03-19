import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

print("Obraz załadowany prawidłowo")

cv2.imshow("Original", image)

resized = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

cv2.imshow("Resized", resized)
cv2.waitKey(0)
