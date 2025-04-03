import cv2

image = cv2.imread('example3.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_small = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel_large = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

dilation_small = cv2.dilate(image, kernel_small, iterations=1)
dilation_large = cv2.dilate(image, kernel_large, iterations=2)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Dylatacja - mały kernel", dilation_small)
cv2.imshow("Dylatacja - duży kernel", dilation_large)

cv2.waitKey(0)
cv2.destroyAllWindows()