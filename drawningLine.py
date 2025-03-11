import numpy as np
import cv2

image = np.zeros((300, 300, 2), np.uint8)
green = (0,255,0)
cv2.line(image,(0,0),(300,300),green)
cv2.imshow("image",image)
cv2.waitKey(0)
