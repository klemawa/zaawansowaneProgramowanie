import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

fragment = image[0:100, 0:100]

image[image.shape[0]-100:, image.shape[1]-100:] = fragment

cv2.imshow('Modified Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
