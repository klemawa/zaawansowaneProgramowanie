import cv2
import numpy as np

image = cv2.imread('example.png')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

s_lowered = cv2.subtract(s, 50)
s_lowered = np.clip(s_lowered, 0, 255) 

s_raised = cv2.add(s, 50)
s_raised = np.clip(s_raised, 0, 255)

hsv_lowered = cv2.merge([h, s_lowered, v])
hsv_raised = cv2.merge([h, s_raised, v])

image_lowered = cv2.cvtColor(hsv_lowered, cv2.COLOR_HSV2BGR)
image_raised = cv2.cvtColor(hsv_raised, cv2.COLOR_HSV2BGR)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Obraz po obniżeniu nasycenia", image_lowered)
cv2.imshow("Obraz po zwiększeniu nasycenia", image_raised)

cv2.waitKey(0)
cv2.destroyAllWindows()
