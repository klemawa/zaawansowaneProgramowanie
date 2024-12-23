import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Mentyn\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

image = Image.open('C:\\Users\\Mentyn\\Desktop\\obrazek.jpg')
text = pytesseract.image_to_string(image)
print(text)


