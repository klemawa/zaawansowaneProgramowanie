import cv2

image = cv2.imread('fanta.png')
template = cv2.imread('fantalogo.png')

imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGrey = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGrey, templateGrey, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
cv2.imshow("Template", template)
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()