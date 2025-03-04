import cv2

image_gray = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread("example.png", cv2.IMREAD_COLOR)

cv2.imshow("Obraz w skali szarości", image_gray)
cv2.imshow("Obraz kolorowy", image_color)

cv2.waitKey(0)
cv2.destroyAllWindows()