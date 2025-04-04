import cv2
import numpy as np

image = cv2.imread('example2.png')
cv2.imshow("Original", image)

kernelSizes = [(3, 3), (9, 9), (15, 15)]

# gaussian blur
for (kX, kY) in kernelSizes:
    blurredGaussian = cv2.GaussianBlur(image, (kX, kY), 0)
    # Generowanie szumu normalnego
    noise = np.zeros_like(blurredGaussian, dtype=np.int16)
    cv2.randn(noise, 0, 25)  # Średnia = 0, odchylenie = 25
    noisy_gaussian = cv2.add(blurredGaussian, noise, dtype=cv2.CV_8U)  # Dodanie szumu

    cv2.imshow(f"Gaussian Blur ({kX}, {kY}) + Noise", noisy_gaussian)
    cv2.waitKey(0)

#median
for k in (3, 9, 15):
    blurredMedian = cv2.medianBlur(image, k)
    # Generowanie szumu równomiernego
    noise = np.zeros_like(blurredMedian, dtype=np.uint8)
    cv2.randu(noise, 0, 50)  # Szum w zakresie 0-50
    noisy_median = cv2.addWeighted(blurredMedian, 0.8, noise, 0.2, 0)  # Mieszanie obrazu i szumu

    cv2.imshow(f"Median Blur {k} + Noise", noisy_median)
    cv2.waitKey(0)
