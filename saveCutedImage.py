import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

cropped_image = image[0:300, 0:300]

cv2.imwrite('cropped_image.jpg', cropped_image)

cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
