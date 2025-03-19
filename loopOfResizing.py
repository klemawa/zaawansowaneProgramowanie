import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

print("Obraz załadowany prawidłowo")

height, width = image.shape[:2]

for scale in range(100, 301, 20):  # od 100% do 300% z krokiem 20%
    new_width = int(width * scale / 100)
    new_height = int(height * scale / 100)

    resized_image = cv2.resize(image, (new_width, new_height))

    cv2.imshow(f"Zmiana rozmiaru {scale}%", resized_image)

    cv2.waitKey(500)

cv2.destroyAllWindows()
