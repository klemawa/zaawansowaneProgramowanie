import numpy as np
import cv2

image = np.zeros((400, 400, 3), np.uint8)
greenRectangle = cv2.rectangle(image, (0, 0), (100, 50), (0, 255, 0))
cv2.imshow("greenRectangle", image)
redRectangle = cv2.rectangle(image,(300,300),(100,50), (255,0,0))
cv2.imshow('image', image)
cv2.waitKey(0)
