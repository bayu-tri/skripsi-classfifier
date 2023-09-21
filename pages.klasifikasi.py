from helper import *
import streamlit as st

# Fungsi untuk mengklasifikasikan gambar
def classify_image(image):
    # Muat model Anda di sini
    model = keras.models.load_model(os.path.join(os.getcwd(), 'static', 'Model.h5'))

    # Praproses gambar (misalnya, resize dan normalisasi)
    image = image.resize((224, 224))
    image = np.array(image) / 127.5  # Normalisasi nilai piksel menjadi rentang [0, 1]

    image = np.expand_dims(image, axis=0)


    # Melakukan prediksi dengan model
    predictions = model.predict(image)

    # Menampilkan hasil prediksi
    # class_names = list(test_data.class_indices.keys())  # Daftar nama kelas
    class_names = ['Jahe', 'Kencur', 'Kunyit', 'Lengkuas']
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index]

    return predicted_class, confidence

# Tampilan web Streamlit
st.title("Klasifikasi Citra Rimpang")
st.write("Unggah gambar untuk mengklasifikasikannya.")

# Unggah gambar
uploaded_image = st.file_uploader("Pilih gambar...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_image)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)

    # Klasifikasikan gambar saat tombol "Klasifikasikan" ditekan
    if st.button('Klasifikasikan'):
        predicted_class, result_confidence = classify_image(image)
        st.write(f"Hasil Klasifikasi: {predicted_class}")
        st.write(f"Keyakinan: {result_confidence:.2%}")