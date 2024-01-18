import cv2
import easyocr

# Inisialisasi EasyOCR
reader = easyocr.Reader(['id'], gpu=True)  # Ganti 'en' dengan kode bahasa yang sesuai

# Inisialisasi video capture
cap = cv2.VideoCapture(0)  # Gunakan 0 untuk kamera utama, bisa disesuaikan

while True:
    # Baca frame dari video
    ret, frame = cap.read()

    # Lakukan OCR pada frame
    results = reader.readtext(frame)

    # Tampilkan hasil OCR pada frame
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # Gambar kotak dan teks hasil OCR pada frame
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Tampilkan frame
    cv2.imshow('EasyOCR Real-Time', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bebaskan sumber daya
cap.release()
cv2.destroyAllWindows()