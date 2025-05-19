import cv2

img = cv2.imread('example.png')

resized = cv2.resize(img, (300, int(img.shape[0] * 300 / img.shape[1])))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

filtered_contours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 500 <= area <= 5000:
        filtered_contours.append(cnt)

print(f"Liczba konturów przed filtrowaniem: {len(contours)}")
print(f"Liczba konturów po filtrowaniu:    {len(filtered_contours)}")

output = resized.copy()
cv2.drawContours(output, filtered_contours, -1, (0, 255, 0), 2)

cv2.imshow('Kontury po filtrowaniu (500–5000 px)', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
