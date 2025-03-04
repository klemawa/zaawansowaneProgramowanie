import cv2

image_gray = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

(h, w) = image_gray.shape[:2] #tutaj trzeba dwa bo w skali szarości mamy dwa a nie trzy
print(f'width: {w} pixels') #zwracamy tylko wysokość iszerokość
print(f'height: {h} pixels')


