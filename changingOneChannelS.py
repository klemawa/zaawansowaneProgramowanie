import cv2
import numpy as np

image = cv2.imread('example.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
s = np.clip(s+30,0,255)
hsvModified = cv2.merge([h,s,v])
result = cv2.cvtColor(hsvModified,cv2.COLOR_HSV2BGR)
cv2.imshow("Orignal", image)
cv2.imshow("Increased S", result)

cv2.waitKey(0)
cv2.destroyAllWindows()