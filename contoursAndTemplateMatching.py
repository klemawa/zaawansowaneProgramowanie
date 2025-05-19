import cv2
import numpy as np

image = cv2.imread('regal.png')
image = cv2.resize(image, (700, 700))
template = cv2.imread('szablonRegal.png')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

h, w = template_gray.shape[:2]
method = cv2.TM_CCOEFF_NORMED
threshold = 0.5 #w zależności od zdjęcia i szablonu trzeba dopasować

for cnt in contours:
    x, y, cw, ch = cv2.boundingRect(cnt)

    if cw < w//2 or ch < h//2:
        continue

    roi = gray[y:y+ch, x:x+cw]
    roi_resized = cv2.resize(roi, (w, h))  # dopasuj rozmiar

    res = cv2.matchTemplate(roi_resized, template_gray, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= threshold:
        cv2.rectangle(image, (x, y), (x + cw, y + ch), (0, 255, 0), 2)
        cv2.putText(image, f"{max_val:.2f}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

cv2.imshow('Dopasowania konturów', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
