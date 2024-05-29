import os
import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow import keras
from keras.models import load_model
from matplotlib import pyplot
from PIL import Image, ImageOps
import streamlit as st
import rembg

# Fungsi untuk mengklasifikasikan gambar
def classify_image(image):

    # Muat model Anda di sini
    model = load_model(os.path.join(os.getcwd(), 'static', 'Best-Model.h5'))

    image = np.expand_dims(image, axis=0)

    # Melakukan prediksi dengan model
    predictions = model.predict(image)

    # Menampilkan hasil prediksi
    class_names = ['Jahe', 'Kelas Lain', 'Kencur', 'Kunyit', 'Lengkuas']
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index]

    return predicted_class, confidence

# Fungsi untuk mengambil nilai piksel gambar
def get_pixel_values(image):
    width, height = image.size
    pixel_values = []
    for y in range(height):
        for x in range(width):
            pixel_values.append(image.getpixel((x, y)))
    return pixel_values

# Fungsi praproses untuk normalisasi gambar
def preprocess_image(image):
    # Menghapus latar belakang gambar menggunakan rembg
    image = np.array(rembg.remove(image).convert('RGB'))
    # Normalisasi gambar
    normalized_image = np.array(image) / 127.5
    return normalized_image


# Tampilan web Streamlit
st.header('KLASIFIKASI RIMPANG MENGGUNAKAN METODE CONVOLUTIONAL NEURAL NETWORK ARSITEKTUR MOBILENETV2')
st.divider()
st.write("Unggah gambar untuk mengklasifikasi.")

# Unggah gambar
uploaded_image = st.file_uploader(
    "Pilih gambar...", type=["jpg", "jpeg"])

if uploaded_image is not None:
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_image).resize((224, 224))

    # Klasifikasikan gambar saat tombol "Klasifikasikan" ditekan
    if st.button('Klasifikasikan'):
        
         with st.expander("🌼 Citra Original"):
            st.image(image, width=300, caption="Citra Hasil Normalisasi")
            st.write("Matrik Citra Original :")
            # Mendapatkan nilai piksel gambar
            pixel_values = get_pixel_values(image)

            # Membuat DataFrame dari nilai piksel
            df = pd.DataFrame(pixel_values, columns=["Red", "Green", "Blue"])
            
            st.write(df)

         # Normalisasi gambar
         normalized_image = preprocess_image(image)

         with st.expander("🎨 Citra Hasil Preprocessing"):
            st.image(normalized_image, width=300, clamp=True, caption="Citra Hasil Normalisasi")
            st.write("Matrik Citra Normalisasi :")
            # Mendapatkan nilai piksel gambar yang sudah dinormalisasi
            normalized_pixel_values = normalized_image.reshape(-1, 3)  # Normalisasi

            # Membuat DataFrame dari nilai piksel yang sudah dinormalisasi
            df_normalized = pd.DataFrame(normalized_pixel_values, columns=["Red", "Green", "Blue"])

            st.write(df_normalized)

         st.write("Hasil Klasifikasi :")
         # st.image(image, width=224)
         predicted_class, result_confidence = classify_image(normalized_image)
         if predicted_class == 'Kelas Lain':
               st.error(
                  f"Citra masukkan bukan salah satu dari rimpang ***Jahe***, ***Kencur***, ***Kunyit*** atau ***Lengkuas***", icon="ℹ️")
         else:
               st.info(
                f"Hasil klasifikasi citra tersebut adalah ***{predicted_class}***", icon="ℹ️")