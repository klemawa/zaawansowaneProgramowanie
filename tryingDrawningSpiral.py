import numpy as np
import cv2

image = np.zeros((300, 300, 3), np.uint8)
cv2.imshow("image", image)
cv2.waitKey(0)

(h,w) = image.shape[:2]
(cX, cY) = (w//2,h//2)

for size in range(20, 300, 20):
    top_left = (cX - size // 2, cY - size // 2)
    bottom_right = (cX + size // 2, cY + size // 2)
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 1)
    
cv2.imshow("image", image)
cv2.waitKey(0)
