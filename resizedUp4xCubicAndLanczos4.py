import cv2
import numpy as np

image = cv2.imread('example.png')
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

print("Obraz załadowany prawidłowo")

new_width = image.shape[1] * 4
new_height = image.shape[0] * 4

resized_cubic = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

resized_cubic = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)


def calculate_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    sharpness = laplacian.var()#wariancja

    return sharpness

sharpness_cubic = calculate_sharpness(resized_cubic)
sharpness_lanczos = calculate_sharpness(resized_lanczos)

print(f"Ostrość obrazu z INTER_CUBIC: {sharpness_cubic}")
print(f"Ostrość obrazu z INTER_LANCZOS4: {sharpness_lanczos}")

cv2.imshow("Oryginalny", image)
cv2.imshow("INTER_CUBIC", resized_cubic)
cv2.imshow("INTER_LANCZOS4", resized_lanczos)

cv2.waitKey(0)
cv2.destroyAllWindows()