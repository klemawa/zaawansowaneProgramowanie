import cv2

img = cv2.imread('fanta.png', cv2.IMREAD_COLOR)
template = cv2.imread('fantalogo.png', cv2.IMREAD_COLOR)
h, w = template.shape[:2]

methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED
]

for method in methods:
    img_display = img.copy()
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img_display, top_left, bottom_right, (0, 0, 255), 2)

    print(f"Metoda: {method}")
    print(f"min_val: {min_val}, max_val: {max_val}")
    cv2.imshow(f'Metoda {method}', img_display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#najlepiej TM_CCOEFF_NORMED i TM_CCORR_NORMED