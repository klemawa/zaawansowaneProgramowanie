import cv2

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mask = cv2.adaptiveThreshold(gray, 255,
                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY_INV,
                             15, 10)

roi = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maska (obiekty)", mask)
cv2.imshow("Wydzielony pierwszy plan (ROI)", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
