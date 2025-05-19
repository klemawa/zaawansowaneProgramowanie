import cv2

img = cv2.imread('example.png')
height, width = img.shape[:2]
new_width = 300
scale = new_width / width
new_height = int(height * scale)
resized = cv2.resize(img, (new_width, new_height))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

modes = {
    "RETR_EXTERNAL": cv2.RETR_EXTERNAL,
    "RETR_LIST": cv2.RETR_LIST,
    "RETR_TREE": cv2.RETR_TREE
}

for mode_name, mode in modes.items():
    contours, hierarchy = cv2.findContours(binary, mode, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = resized.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 2)  # czerwony, grubość 2px
    cv2.imshow(f'Kontury - {mode_name}', contour_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#tree i list najlepeij
