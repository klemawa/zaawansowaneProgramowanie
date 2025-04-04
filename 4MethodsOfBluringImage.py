import cv2

image = cv2.imread('example2.png')
cv2.imshow("Original", image)

#blur
kernelSizes = [(3, 3), (9, 9), (15, 15)]
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

# gaussian blur
for (kX, kY) in kernelSizes:
    blurredGaussian = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurredGaussian)
    cv2.waitKey(0)

#median
for k in (3, 9, 15):
    blurredMedian = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurredMedian)
    cv2.waitKey(0)


#bilateral filter
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for (diameter, sigmaColor, sigmaSpace) in params:
    blurredFilter = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv2.imshow("Filter {}".format(k), blurredFilter)
    cv2.waitKey(0)

#1.najlepiej z szumem adzi sobie median
#2.najlepiej zachowuje szczegóły filter
#3.blur szybki i prosty ale rozmywa szczególy i krawędzie
#gausian blur szybkie, ale nie zachowuje dorze krawędzi
#median bardzo dobrze do typu pieprsz i sól, ale jest wolniejszy
#bilateral zachowuje krawędzie, selektywny, ale wolny i kosztowny obliczeniowo

