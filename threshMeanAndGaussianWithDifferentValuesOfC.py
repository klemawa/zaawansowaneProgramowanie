import cv2

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orignalne", gray)

threshMean1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 2)
threshMean2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)
threshMean3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
threshMean4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 15)

threshGaussian1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 2)
threshGaussian2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)
threshGaussian3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 10)
threshGaussian4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 15)

cv2.imshow("Progowanie adaptacyjne MEAN, C=2", threshMean1)
cv2.imshow("Progowanie adaptacyjne MEAN, C=5", threshMean2)
cv2.imshow("Progowanie adaptacyjne MEAN, C=10", threshMean3)
cv2.imshow("Progowanie adaptacyjne MEAN, C=15", threshMean4)

cv2.imshow("Progowanie adaptacyjne GAUSSIAN, C=2", threshGaussian1)
cv2.imshow("Progowanie adaptacyjne GAUSSIAN, C=5", threshGaussian2)
cv2.imshow("Progowanie adaptacyjne GAUSSIAN, C=10", threshGaussian3)
cv2.imshow("Progowanie adaptacyjne GAUSSIAN, C=15", threshGaussian4)


cv2.waitKey(0)
cv2.destroyAllWindows()