import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd, nie można wczytać obrazu")
else:
    print("Obraz wczytany poprawnie")

cv2.imshow("Original", image)
cv2.waitKey(0)

(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

(b,g,r) = image[20,50]
print("Pixel at (20,50) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

image[20,50] = (0,255,0)
(b,g,r) = image[20,50]
print("Pixel at (50,20) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

cv2.imshow("Changed pixel", image)
cv2.waitKey(0)