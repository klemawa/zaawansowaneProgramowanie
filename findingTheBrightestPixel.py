import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd")
else:
    print("Git")
cv2.imshow('Orginal', image)
cv2.waitKey(0)

maxBrightness = -1  # Najniższa możliwa wartość jasności
maxCoords = (0, 0)  # Współrzędne najjaśniejszego piksela

# Przeszukiwanie całego obrazu
for y in range(image.shape[0]):  # Przechodzimy po wszystkich wierszach
    for x in range(image.shape[1]):  # Przechodzimy po wszystkich kolumnach
        pixel = image[y, x]

        # Obliczenie jasności piksela
        brightness = 0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0]

        # Jeśli jasność tego piksela jest większa niż dotychczasowa
        if brightness > maxBrightness:
            maxBrightness = brightness
            maxCoords = (x, y)

print(f'Najjaśniejszy piksel znajduje się w: {maxCoords}')
print(f'Wartość piksela: B: {image[maxCoords[1], maxCoords[0]][0]}, G: {image[maxCoords[1], maxCoords[0]][1]}, R: {image[maxCoords[1], maxCoords[0]][2]}')

cv2.circle(image, maxCoords, 10, (0,0,0), 1)  # Narysowanie żółtego kółka
cv2.imshow('Obraz z najjaśniejszym pikselem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
