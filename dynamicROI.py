import cv2

image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: Nie udało się wczytać obrazu.")
    exit()

roi_width = 100
roi_height = 100

x = 0

while True:
    roi = image[0:roi_height, x:x + roi_width]

    cv2.imshow('Moving ROI', roi)

    key = cv2.waitKey(100) & 0xFF

    if key == ord('q'):
        break

    x += 10
    if x + roi_width > image.shape[1]:
        x = 0

cv2.destroyAllWindows()
