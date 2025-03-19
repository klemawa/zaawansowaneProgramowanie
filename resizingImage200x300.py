import cv2
import imutils

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

print("Obraz załadowany prawidłowo")
cv2.imshow("Original", image)
cv2.waitKey(0)

methods = [
("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
for (name, method) in methods:
    print("[INFO] {}".format(name))
    resized = imutils.resize(image, width=image.shape[1] * 3,inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)

cv2.destroyAllWindows()