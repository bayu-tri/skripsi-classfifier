import streamlit as st
from libs import *

# Fungsi untuk mengklasifikasikan gambar
def classify_image(image):

    # Muat model Anda di sini
    model = load_model(os.path.join(os.getcwd(), 'static', 'Model.h5'))

    # Praproses gambar
    image = np.array(image)  # Konversi gambar ke tipe data NumPy
    image = image / 127.5

    image = np.expand_dims(image, axis=0)

    # Melakukan prediksi dengan model
    predictions = model.predict(image)

    # Menampilkan hasil prediksi
    class_names = ['Jahe', 'Kelas Lain', 'Kencur', 'Kunyit', 'Lengkuas']
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index]

    return predicted_class, confidence

# Tampilan web Streamlit
st.title("Klasifikasi Citra Rimpang")
st.write("Unggah gambar untuk mengklasifikasikannya.")

# Unggah gambar
uploaded_image = st.file_uploader(
    "Pilih gambar...", type=["jpg", "jpeg"])

if uploaded_image is not None:
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_image).resize((224, 224))
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)

    # Klasifikasikan gambar saat tombol "Klasifikasikan" ditekan
    if st.button('Klasifikasikan'):

        st.image(image, width=224)
        predicted_class, result_confidence = classify_image(image)
        if predicted_class == 'Kelas Lain':
            st.error(
                f"Citra masukkan bukan salah satu dari rimpang ***Jahe***, ***Kencur***, ***Kunyit*** atau ***Lengkuas***", icon="ℹ️")
        else:
            st.info(
                f"Hasil klasifikasi citra tersebut adalah ***{predicted_class}***", icon="ℹ️")
