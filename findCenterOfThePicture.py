import cv2

image = cv2.imread('example.png')

if image is None:
    print("Błąd")
else:
    print("Git")

(h,w) = image.shape[:2]
(cX, cY) = (w//2,h//2)
print(f'Środek; ({cX}, {cY})')

(b,g,r) = image[cX,cY]
print("Pixel at center - Red: {}, Green: {}, Blue: {}".format(r,g,b))

