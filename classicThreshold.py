import cv2

img = cv2.imread('example.png')

original_height, original_width = img.shape[:2]
new_width = 300
scale = new_width / original_width
new_height = int(original_height * scale)
resized_img = cv2.resize(img, (new_width, new_height))

gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

threshold_values = [100, 140, 180]

for thresh in threshold_values:
    _, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    window_name = f'Progowanie: {thresh}'
    cv2.imshow(window_name, binary)

cv2.imshow('Obraz oryginalny (przeskalowany)', resized_img)
cv2.imshow('Odcienie szarosci', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
