import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

print("Obraz załadowany prawidłowo")

new_width = 800

height, width = image.shape[:2]
new_height = int((new_width / width) * height)
resized_image = cv2.resize(image, (new_width, new_height))

cv2.imshow("Powiększony obraz", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('resized_output.png', resized_image)

print("Obraz zapisany jako resized_output.png")
