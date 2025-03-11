import numpy as np
import cv2

image = np.zeros((300, 300, 3), np.uint8)
cv2.imshow("image", image)
cv2.waitKey(0)

red = (0,0,255)#kwadrat
blue = (255,0,0)#okrąg

(h,w) = image.shape[:2]
(cX, cY) = (w//2,h//2)
star = (cX - 50, cY - 50)
end = (cX + 50, cY + 50)

cv2.rectangle(image, star, end, red, 2)
for r in range(0, 50, 25):
    cv2.circle(image, (cX, cY), r, blue)
cv2.imshow("image", image)
cv2.waitKey(0)

