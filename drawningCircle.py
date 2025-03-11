import numpy as np
import cv2

image = np.zeros((300, 300, 3), np.uint8)
cv2.imshow("image", image)
cv2.waitKey(0)
blue = (0,0,255)#40px
red = (255,0,0)#60px
(cX,cY) = (image.shape[1]//2, image.shape[0]//2)
for r in range(0,40,25):
    cv2.circle(image,(50,50),r,blue)
for t in range(0,60,25):
    cv2.circle(image,(250,250),t,red)
cv2.imshow("image", image)
cv2.waitKey(0)