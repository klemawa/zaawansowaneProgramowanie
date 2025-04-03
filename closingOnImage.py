import cv2

image = cv2.imread('example5.png')

kernel_sizes = [(3, 3), (5, 5), (7, 7)]

cv2.imshow("Oryginalny obraz", image)

for ksize in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Zamknięcie: {ksize}", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
