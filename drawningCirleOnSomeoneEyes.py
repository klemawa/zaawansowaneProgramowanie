import cv2

image = cv2.imread('typo.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Rysowanie elementów na zdjęciu
for (x, y, w, h) in faces:
    # Niebieski okrąg wokół twarzy
    cv2.circle(image, (x + w // 2, y + h // 2), w // 2, (255, 0, 0), 2)

    # Wykrywanie oczu wewnątrz wykrytej twarzy
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]
    eyes = eyes_cascade.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        # Czerwone koła na oczach
        cv2.circle(roi_color, (ex + ew // 2, ey + eh // 2), ew // 2, (0, 0, 255), -1)

    # Zielony prostokąt na ustach (przybliżone położenie)
    mouth_y = y + int(h * 0.75)  # Przybliżona wysokość ust
    cv2.rectangle(image, (x, mouth_y), (x + w, mouth_y + 20), (0, 255, 0), -1)

# Wyświetlenie obrazu
cv2.imshow("Zamazane zdjęcie", image)
cv2.waitKey(0)
