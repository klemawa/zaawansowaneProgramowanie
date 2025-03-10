import cv2

image = cv2.imread('example.png')
if image is None:
    print("Błąd")
else:
    print("Git")
cv2.imshow('Orginal', image)
cv2.waitKey(0)

pixel1 = image[50,50]
print("Pixel at (50,50) - Red: {}, Green: {}, Blue: {}".format(pixel1[0], pixel1[1], pixel1[2]))

pixel2 = image[200,200]
print("Pixel at (200,200) - Red: {}, Green: {}, Blue: {}".format(pixel2[0], pixel2[1], pixel2[2]))

roznicaB = abs(pixel2[0] - pixel1[0])
roznicaG = abs(pixel2[1] - pixel1[1])
roznicaR = abs(pixel2[2] - pixel1[2])

print(f'Różnice w wartościach kanałów:')
print(f'Różnica w kanale B: {roznicaB}')
print(f'Różnica w kanale G: {roznicaG}')
print(f'Różnica w kanale R: {roznicaR}')