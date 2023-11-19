import streamlit as st
from helper import *

# Fungsi untuk mengklasifikasikan gambar


def classify_image_treshold(image):

    # Muat model Anda di sini
    model = load_model(os.path.join(os.getcwd(), 'static', 'Model.h5'))

    # Praproses gambar (misalnya, resize dan normalisasi)
    # image = image.resize((224, 224))  # Resize gambar menggunakan cv2
    image = np.array(image)  # Konversi gambar ke tipe data NumPy
    image = image / 127.5

    image = np.expand_dims(image, axis=0)

    # Melakukan prediksi dengan model
    predictions = model.predict(image)
    threshold = 0.5

    # Menampilkan hasil prediksi
    class_names = ['Jahe', 'Kelas Lain', 'Kencur', 'Kunyit', 'Lengkuas']

    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index]

    if confidence > threshold:
        predicted_class = predicted_class
        confidence = confidence
    else:
        predicted_class = 'Kelas lain'
        confidence = 0

    return predicted_class, confidence


def classify_image_no_treshold(image):

    # Muat model Anda di sini
    model = load_model(os.path.join(os.getcwd(), 'static', 'Model.h5'))

    # Praproses gambar (misalnya, resize dan normalisasi)
    # image = image.resize((224, 224))  # Resize gambar menggunakan cv2
    image = np.array(image)  # Konversi gambar ke tipe data NumPy
    image = image / 127.5

    image = np.expand_dims(image, axis=0)

    # Melakukan prediksi dengan model
    predictions = model.predict(image)

    # Menampilkan hasil prediksi
    # class_names = list(test_data.class_indices.keys())  # Daftar nama kelas
    class_names = ['Jahe', 'Kelas Lain', 'Kencur', 'Kunyit', 'Lengkuas']
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index]

    return predicted_class, confidence


# def rotate_image(image):
#     image = np.array(image)
#     # Augmentasi citra dengan rotasi
#     rotation_angle_right = 40  # Sudut rotasi (misalnya 30 derajat)
#     rotation_angle_left = -40  # Sudut rotasi (misalnya 30 derajat)

#     rows, cols, _ = image.shape

#     rotation_matrix = cv2.getRotationMatrix2D(
#         (cols / 2, rows / 2), rotation_angle_right, 1)
#     rotated_image_right = cv2.warpAffine(image, rotation_matrix, (cols, rows))
#     rotation_matrix = cv2.getRotationMatrix2D(
#         (cols / 2, rows / 2), rotation_angle_left, 1)
#     rotated_image_left = cv2.warpAffine(image, rotation_matrix, (cols, rows))

#     return rotated_image_right, rotated_image_left


# def brightness_image(image):
#     image = np.array(image)

#     # Augmentasi citra dengan perubahan brightness
#     # Faktor brightness (misalnya 1.5 untuk peningkatan brightness)
#     brightness_factor_plus = 1.4
#     # Faktor brightness (misalnya 1.5 untuk peningkatan brightness)
#     brightness_factor_minus = 0.6

#     brightened_image = cv2.convertScaleAbs(
#         image, alpha=brightness_factor_plus, beta=0)
#     darkened_image = cv2.convertScaleAbs(
#         image, alpha=brightness_factor_minus, beta=0)

#     return brightened_image, darkened_image


# def shear_image(image):
#     image = np.array(image)

#     # Mengatur parameter shear
#     shear_factor_x = 0.1  # Shear dalam arah sumbu X
#     shear_factor_y = 0.1  # Shear dalam arah sumbu Y

#     # Mendapatkan matriks transformasi shear
#     shear_matrix = np.array([[1, shear_factor_x, 0], [shear_factor_y, 1, 0]])

#     # Melakukan shear pada citra
#     sheared_image = cv2.warpAffine(
#         image, shear_matrix, (image.shape[1], image.shape[0]))
#     return sheared_image


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

    # rotated_image_right, rotated_image_left = rotate_image(image)
    # brightened_image, darkened_image = brightness_image(image)
    # shear_image = shear_image(image)

    # Klasifikasikan gambar saat tombol "Klasifikasikan" ditekan
    if st.button('Klasifikasikan'):

        # tab1, tab2, tab3, tab4 = st.tabs(
        tab1 = st.tabs(
            ["Hasil Klasifikasi :"])
        with tab1:
            st.image(image, width=224)
            predicted_class, result_confidence = classify_image_treshold(image)
            st.info(
                # f"Hasil klasifikasi citra Asli adalah ***{predicted_class}***,nilai keyakinan ***{result_confidence:.2%}***", icon="ℹ️")
                f"Hasil klasifikasi citra tersebut adalah ***{predicted_class}***", icon="ℹ️")

        # with tab2:
        #     st.image(image, width=224)
        #     predicted_class, result_confidence = classify_image_no_treshold(
        #         image)
        #     st.info(
        #         f"Hasil klasifikasi citra Asli adalah ***{predicted_class}***,nilai keyakinan ***{result_confidence:.2%}***", icon="ℹ️")

        # with tab2:
        #     col1, col2 = st.columns(2)

        #     with col1:
        #         st.image(rotated_image_right, width=224)
        #         predicted_class, result_confidence = classify_image(
        #             rotated_image_right)
        #         st.info(
        #             f"Hasil klasifikasi citra Rotasi 30° Ke Kiri adalah ***{predicted_class}***, nilai keyakinan ***{result_confidence:.2%}***", icon="ℹ️")

        #     with col2:
        #         st.image(rotated_image_left, width=224)
        #         predicted_class, result_confidence = classify_image(
        #             rotated_image_left)
        #         st.info(
        #             f"Hasil klasifikasi citra Rotasi 30° Ke Kanan adalah ***{predicted_class}***, nilai keyakinan ***{result_confidence:.2%}***", icon="ℹ️")

        # with tab3:
        #     col1, col2 = st.columns(2)

        #     with col1:
        #         st.image(brightened_image, width=224)
        #         predicted_class, result_confidence = classify_image(
        #             brightened_image)
        #         st.info(
        #             f"Hasil klasifikasi citra Kecarahan +50% adalah ***{predicted_class}***, nilai keyakinan ***{result_confidence:.2%}***", icon="ℹ️")

        #     with col2:
        #         st.image(darkened_image, width=224)
        #         predicted_class, result_confidence = classify_image(
        #             darkened_image)
        #         st.info(
        #             f"Hasil klasifikasi citra Kecarahan -50% adalah ***{predicted_class}***, nilai keyakinan ***{result_confidence:.2%}***", icon="ℹ️")

        # with tab4:
        #     st.image(shear_image, width=224)
        #     predicted_class, result_confidence = classify_image(shear_image)
        #     st.info(
        #         f"Hasil klasifikasi citra Shear adalah ***{predicted_class}***, nilai keyakinan ***{result_confidence:.2%}***", icon="ℹ️")

            # st.image(zoomed_out_image, width=224)
            # predicted_class, result_confidence = classify_image(zoomed_out_image)
            # st.info(f"Hasil klasifikasi citra yang diperkecil 60% adalah {predicted_class}, dengan nilai keyakinan {result_confidence:.2%}", icon="ℹ️")
