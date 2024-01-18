from PIL import Image, ImageEnhance
import pytesseract
import re
# import cv2
# import numpy as np

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

# Load the image
image_path = 'contoh/ktp3.jpg'
# original_image = cv2.imread(image_path)

# # Convert the image to grayscale
# resized_image = cv2.resize(original_image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# # Convert the image to grayscale
# gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# # Enhance contrast
# contrast = ImageEnhance.Contrast(Image.fromarray(gray_image))
# contrast_image = contrast.enhance(2.0)  # You can adjust the enhancement factor

# # Enhance sharpness
# sharpness = ImageEnhance.Sharpness(contrast_image)
# enhanced_image = sharpness.enhance(2.0)  # You can adjust the enhancement factor

# # Apply adaptive thresholding
# _, threshold_image = cv2.threshold(np.array(enhanced_image), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


# Simple image to string
hasil = pytesseract.image_to_string(Image.open(image_path))

# Cleaning
hasil_bersih = re.sub(r'\s+', ' ', hasil.strip())
print(hasil_bersih)

# Pattern Format
nik_pattern = re.compile(r'\b3.{15,17}\b')



# Format lain
# nama_pattern = re.compile(r'Nama\s*:\s*([a-zA-Z\s]+)\s*Tempat/Tg!', re.IGNORECASE)
# ttl_pattern = re.compile(r'Tempat/Tgi\s*Lahir\s*\+?:\s*([^\n]+)\s*Jenis', re.IGNORECASE)
# goldar_pattern = re.compile(r'Gol.\s*Darah\s*:\s*([a-zA-Z\s]+)\s*Alamat', re.IGNORECASE)
# alamat_pattern = re.compile(r'Alamat\s*:\s*([^\n]+)\s*RT/RW', re.IGNORECASE)
# rt_pattern = re.compile(r'RT/RW\s*:\s*([^\n]+)\s*Kel/Desa', re.IGNORECASE)
# desa_pattern = re.compile(r'Kel/Desa\s*:\s*([^\n]+)\s*Kecamatan', re.IGNORECASE)
# kec_pattern = re.compile(r'Kecamatan\s*:\s*([^\n]+)\s*Agama', re.IGNORECASE)
# agama_pattern = re.compile(r'Agama\s*:\s*([^\n]+)\s*Status', re.IGNORECASE)

# Search
match_nik = nik_pattern.search(hasil_bersih)

# match_nama = nama_pattern.search(hasil_bersih)
# match_ttl = ttl_pattern.search(hasil_bersih)
# match_goldar = goldar_pattern.search(hasil_bersih)
# match_alamat = alamat_pattern.search(hasil_bersih)
# match_rt = rt_pattern.search(hasil_bersih)
# match_desa = desa_pattern.search(hasil_bersih)
# match_kec = kec_pattern.search(hasil_bersih)
# match_agama = agama_pattern.search(hasil_bersih)


# Make Variable
nik = match_nik.group() if match_nik else ""
if 'e' in nik:
    if len(nik) == 16:
        nik = nik.replace('e', '2')
    elif len(nik) > 16:
        nik = nik.replace('e', '')
# nama = match_nama.group(1) if match_nama else ""
# ttl = match_ttl.group(1) if match_ttl else ""
# goldar = match_goldar.group(1) if match_goldar else ""
# alamat = match_alamat.group(1) if match_alamat else ""
# rt = match_rt.group(1) if match_rt else ""
# desa = match_desa.group(1) if match_desa else ""
# kec = match_kec.group(1) if match_kec else ""
# agama = match_agama.group(1) if match_agama else ""

# Print
print("NIK   :", nik)
# print("Nama  :", nama)
# print("TTL   :", ttl)
# print("Goldar:", goldar)
# print("Alamat:", alamat)
# print("RT/RW :", rt)
# print("Desa  :", desa)
# print("Kec.  :", kec)
# print("Agama :", agama)
