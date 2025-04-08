import cv2

image = cv2.imread('example2.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T30, thresh30) = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
(T100, thresh100) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
(T200, thresh200) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

cv2.imshow("Progowanie T = 30", thresh30)
cv2.imshow("Progowanie T = 100", thresh100)
cv2.imshow("Progowanie T = 200", thresh200)

cv2.waitKey(0)
cv2.destroyAllWindows()
