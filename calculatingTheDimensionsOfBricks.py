import cv2

img = cv2.imread('example.png')

height, width = img.shape[:2]
new_width = 500
scale = new_width / width
new_height = int(height * scale)
resized = cv2.resize(img, (new_width, new_height))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

annotated_img = resized.copy()

for i, contour in enumerate(contours, start=1):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(annotated_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    text = f'{w}x{h} px'
    cv2.putText(annotated_img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 1, cv2.LINE_AA)

cv2.imshow('Wymiary kostek', annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
