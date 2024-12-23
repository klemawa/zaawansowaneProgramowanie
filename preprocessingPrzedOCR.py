import cv2
import pytesseract
import matplotlib.pyplot as plt


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = cv2.imread(r'C:\Users\Klementyna\PycharmProjects\zaawansowaneProgramowanie\zdj1.png')
img2 = cv2.imread(r'C:\Users\Klementyna\PycharmProjects\zaawansowaneProgramowanie\zdj2.png')

if img is None:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku.")
else:
    #skala szarości
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Metoda 1: MedianBlur
    median_img = cv2.medianBlur(gray_img, 3)

    # Metoda 2: Gaussian Blur
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Metoda 3: Bilateral Filter
    bilateral_img = cv2.bilateralFilter(gray_img, 9, 75, 75)

    # Metoda 4: Adaptive Thresholding
    adaptive_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Metoda 5: Gaussian Blur i binaryzacja z Otsu
    _, threshold_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Metoda 6: Bilateral Filter i binaryzacja z Otsu
    _, bilateral_threshold_img = cv2.threshold(bilateral_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    plt.subplot(231), plt.imshow(median_img, cmap='gray'), plt.title('MedianBlur')
    plt.subplot(232), plt.imshow(blurred_img, cmap='gray'), plt.title('Gaussian Blur')
    plt.subplot(233), plt.imshow(bilateral_img, cmap='gray'), plt.title('Bilateral Filter')
    plt.subplot(234), plt.imshow(adaptive_img, cmap='gray'), plt.title('Adaptive Threshold')
    plt.subplot(235), plt.imshow(threshold_img, cmap='gray'), plt.title('Gaussian + Otsu')
    plt.subplot(236), plt.imshow(bilateral_threshold_img, cmap='gray'), plt.title('Bilateral + Otsu')

    plt.show()

    # Wybór metody (np. Gaussian + Otsu)
    tekst = pytesseract.image_to_string(threshold_img)
    print("Wykryty tekst:")
    print(tekst)


if img2 is None:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku.")
else:
    #skala szarości
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Metoda 1: MedianBlur
    median_img2 = cv2.medianBlur(gray_img2, 3)

    # Metoda 2: Gaussian Blur
    blurred_img2 = cv2.GaussianBlur(gray_img2, (5, 5), 0)

    # Metoda 3: Bilateral Filter
    bilateral_img2 = cv2.bilateralFilter(gray_img2, 9, 75, 75)

    # Metoda 4: Adaptive Thresholding
    adaptive_img2 = cv2.adaptiveThreshold(gray_img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Metoda 5: Gaussian Blur i binaryzacja z Otsu
    _, threshold_img2 = cv2.threshold(blurred_img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Metoda 6: Bilateral Filter i binaryzacja z Otsu
    _, bilateral_threshold_img = cv2.threshold(bilateral_img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    plt.subplot(231), plt.imshow(median_img2, cmap='gray'), plt.title('MedianBlur')
    plt.subplot(232), plt.imshow(blurred_img2, cmap='gray'), plt.title('Gaussian Blur')
    plt.subplot(233), plt.imshow(bilateral_img2, cmap='gray'), plt.title('Bilateral Filter')
    plt.subplot(234), plt.imshow(adaptive_img2, cmap='gray'), plt.title('Adaptive Threshold')
    plt.subplot(235), plt.imshow(threshold_img2, cmap='gray'), plt.title('Gaussian + Otsu')
    plt.subplot(236), plt.imshow(bilateral_threshold_img, cmap='gray'), plt.title('Bilateral + Otsu')

    plt.show()

    # Wybór metody (np. Gaussian + Otsu)
    tekst2 = pytesseract.image_to_string(threshold_img2)
    print("Wykryty tekst:")
    print(tekst2)
