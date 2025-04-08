import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()
cv2.imshow('RGB', image)
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)
cv2.waitKey(0)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()