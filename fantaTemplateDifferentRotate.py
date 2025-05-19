import cv2

image = cv2.imread('fanta.png')
template = cv2.imread('fantalogo.png')

if template.shape[0] > image.shape[0] or template.shape[1] > image.shape[1]:
    template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

(startX, startY) = maxLoc
(endX, endY) = (startX + template.shape[1], startY + template.shape[0])

cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 3)

cv2.imshow("Wynik", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Wykryte logo na współrzędnych: ({startX}, {startY})")
print(f"Wartość dopasowania: {maxVal:.4f}")
