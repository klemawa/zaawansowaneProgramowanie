import cv2

image_color = cv2.imread("example.png", cv2.IMREAD_COLOR)
cv2.imshow("Obraz kolorowy", image_color)

resized_image = cv2.resize(image_color, (800, 600))
cv2.imshow("Obraz kolorowy display", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
