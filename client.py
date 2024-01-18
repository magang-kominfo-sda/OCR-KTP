import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("Aplikasi Pengunggahan dan Tampil Foto")

# Widget untuk mengunggah file gambar
uploaded_file = st.file_uploader("Pilih sebuah file gambar", type=["jpg", "jpeg", "png"])

# Jika file gambar telah diunggah
if uploaded_file is not None:
    # Tampilkan gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)
    st.write("Ukuran gambar:", image.size)
