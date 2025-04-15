import cv2

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orignalne", gray)

thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)
thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
thresh3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 10)
thresh4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 41, 10)

cv2.imshow("Progowanie adaptacyjne MEAN,block size: 11", thresh1)
cv2.imshow("Progowanie adaptacyjne MEAN,block size: 21", thresh2)
cv2.imshow("Progowanie adaptacyjne MEAN,block size: 31", thresh3)
cv2.imshow("Progowanie adaptacyjne MEAN,block size: 41", thresh4)

cv2.waitKey(0)
cv2.destroyAllWindows()