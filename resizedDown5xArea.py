import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

print("Obraz załadowany prawidłowo")

new_width = image.shape[1] // 5
new_height = image.shape[0] // 5

resized_area = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Wyświetlenie wyników
cv2.imshow("Oryginalny", image)
cv2.imshow("INTER_AREA (najlepsza jakość przy zmniejszaniu)", resized_area)


cv2.waitKey(0)
cv2.destroyAllWindows()
