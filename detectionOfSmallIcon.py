import cv2

screenshot = cv2.imread('pelnyscreen.png')
icon = cv2.imread('ikonka.png')

method = cv2.TM_CCOEFF_NORMED
result = cv2.matchTemplate(screenshot, icon, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + icon.shape[1], top_left[1] + icon.shape[0])

cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

print(f'Max dopasowanie: {max_val}')

cv2.imshow('Wynik dopasowania', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
