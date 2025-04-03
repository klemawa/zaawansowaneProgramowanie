import cv2

image = cv2.imread('example3.png', cv2.IMREAD_GRAYSCALE)

shapes = {
    "Kwadrat": cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
    "Krzyż": cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)),
    "Elipsa": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
}

for name, kernel in shapes.items():
    # Zastosowanie operacji morfologicznych
    erosion = cv2.erode(image, kernel, iterations=1)
    dilation = cv2.dilate(image, kernel, iterations=1)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

    # Wyświetlenie wyników
    cv2.imshow(f"{name} - Oryginalny", image)
    cv2.imshow(f"{name} - Erozja", erosion)
    cv2.imshow(f"{name} - Dylatacja", dilation)
    cv2.imshow(f"{name} - Otwarcie", opening)
    cv2.imshow(f"{name} - Zamknięcie", closing)
    cv2.imshow(f"{name} - Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()