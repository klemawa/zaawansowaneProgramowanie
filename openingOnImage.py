import cv2

image = cv2.imread('example5.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original', gray)

kernelSizes = [(3,3), (5,5), (7,7)]

for ksize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opening: {ksize}", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
