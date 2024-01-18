import easyocr
import re

# Inisialisasi EasyOCR
reader = easyocr.Reader(['id'])

# Baca teks dari gambar
result = reader.readtext('contoh/ktp3.jpg')

nik_pattern = re.compile(r'\b3.{13,19}\b')

all_niks = []

for _, text, _ in result:
    match_nik = nik_pattern.search(text)
    nik = match_nik.group() if match_nik else None  # Use None for invalid NIKs
    if nik:
        all_niks.append(nik)

# Print
print("NIK   :", all_niks[0])
