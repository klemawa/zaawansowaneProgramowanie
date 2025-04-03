import cv2

image = cv2.imread('example3.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

erosion_square = cv2.erode(gray, kernel_square, iterations=1)
erosion_ellipse = cv2.erode(gray, kernel_ellipse, iterations=1)

cv2.imshow("Oryginalny obraz", gray)
cv2.imshow("Erozja - kwadratowy kernel", erosion_square)
cv2.imshow("Erozja - eliptyczny kernel", erosion_ellipse)

cv2.waitKey(0)
cv2.destroyAllWindows()
