import cv2

image = cv2.imread('example.png')

if image is None:
    print("Błąd")
else:
    print("Git")



print("Podaj współrzędne x i y: ")
while True:
    maxX = image.shape[1]
    maxY = image.shape[0]
    x = int(input())
    y = int(input())
    if (x > maxX) or (y > maxY):
        print("Podane Współrzędne są za duże. Spróbuj ponownie:")
    else:
        print("Współrzędne poprawne")
        image[y, x] = (0, 0, 0)
        (b, g, r) = image[y, x]
        cv2.imshow(f"Black pixel at ({x},{y})", image)
        cv2.waitKey(0)
        break



