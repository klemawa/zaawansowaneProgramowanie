import cv2

image = cv2.imread('exampleFace.png')

if image is None:
    print("Błąd: Nie udało się wczytać obrazu. Sprawdź ścieżkę pliku.")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#kadrowanie obrazu na podstawie wykrytej twarzy
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Detected Face', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
