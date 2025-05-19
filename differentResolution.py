import cv2

img = cv2.imread('example.png')
scales = [1.0, 0.5, 0.25]

for scale in scales:
    new_size = (int(img.shape[1] * scale), int(img.shape[0] * scale))
    resized = cv2.resize(img, new_size)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_img = resized.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 2)

    window_title = f'Skala: {int(scale * 100)}'
    cv2.imshow(window_title, contour_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
