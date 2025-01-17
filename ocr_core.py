try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract



def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\SOULEYSANOGO\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
    print("Filename ....", filename)
    text_from_image = pytesseract.image_to_string(Image.open(filename)) 
    print("text_from_image :",text_from_image)
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text_from_image  
    # Then we will pr.image_to_stringint the text in the image
