import cv2

img = cv2.imread('example.png')
scale = 1.0
resized = cv2.resize(img, (0, 0), fx=scale, fy=scale)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = resized.copy()
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    cx, cy = x + w // 2, y + h // 2

    cv2.putText(output, str(i + 1), (cx - 10, cy - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.drawContours(output, [cnt], -1, (0, 0, 255), 2)

cv2.imshow('Numerowane kostki', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
