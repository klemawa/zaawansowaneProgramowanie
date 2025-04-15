import cv2

image = cv2.imread('example2.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orignalne", gray)

binary = cv2.adaptiveThreshold(gray, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV,
                               blockSize=15,
                               C=10)
cv2.imshow("Tekst po progowaniu (binarne)", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()