# test_pytesseract.py

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\SOULEYSANOGO\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


#text_from_image = pytesseract.image_to_string(Image.open('test_image.png'))
text_from_image = pytesseract.image_to_string(Image.open('D:/code/PYTHON/OCR/python-ocr-example/static/uploads/ocr_image_1.png'))

print(text_from_image)