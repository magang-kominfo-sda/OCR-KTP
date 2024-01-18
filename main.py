from PIL import Image, ImageEnhance
import pytesseract
import re
# import cv2
# import numpy as np

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
pytesseract.pytesseract.OPTICN_GPU_LAYOUT_MODE = 6

# Load the image
image_path = 'contoh/ktp3.jpg'

# Simple image to string
hasil = pytesseract.image_to_string(Image.open(image_path))

# Cleaning
hasil_bersih = re.sub(r'\s+', ' ', hasil.strip())
print(hasil_bersih)

# Pattern Format
nik_pattern = re.compile(r'\b3.{13,19}\b')

# Search
match_nik = nik_pattern.search(hasil_bersih)

# Make Variable
nik = match_nik.group() if match_nik else ""
if 'e' in nik:
    if len(nik) == 16:
        nik = nik.replace('e', '2')
    elif len(nik) > 16:
        nik = nik.replace('e', '')

#Print
print("NIK   :", nik)

