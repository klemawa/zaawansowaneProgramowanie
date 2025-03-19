import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd")
else:
    print("Git")
cv2.imshow('Orginal', image)
cv2.waitKey(0)
while True:
    try:
        rotation = int(input("Wybierz rotację obrazu: 0 - pionowe, 1 - poziome, -1 - oba: "))
        if rotation in [0, 1, -1]:
            break
        else:
            print("Nieprawidłowa wartość. Wybierz 0, 1 lub -1.")
    except ValueError:
        print("Proszę podać liczbę całkowitą (0, 1 lub -1).")

flipped = cv2.flip(image, rotation)

cv2.imshow('Flipped', flipped)
cv2.waitKey(0)