from st_pages import Page, show_pages
import streamlit as st
from helper import *

# Optional -- adds the title and icon to the current page
# st.subheader(":gray[Tugas Akhir]")
st.header('KLASIFIKASI RIMPANG MENGGUNAKAN METODE CONVOLUTIONAL NEURAL NETWORK ARSITEKTUR MOBILENETV2', divider='rainbow')
# st.caption("Bayu Tri Nugroho (123190015)")

tab1, tab2, tab3 = st.tabs(["Abstrak", "Rumusan Masalah", "Tujuan Penelitian"])

with tab1:
   st.write("Rempah memiliki manfaat di berbagai bidang seperti pada bidang kuliner, kesehatan dan juga kecantikan. Rempah diperoleh dengan mengambil bagian tanaman seperti batang, daun, kulit kayu, umbi, akar, biji, bunga, rimpang serta bagian lainnya (Putra et al., 2023). Salah satu bagian dari tanaman rempah adalah rimpang, dalam ilmu botani merupakan bagian batang tumbuhan yang tumbuhnya menjalar ke bawah permukaan tanah dan dapat menghasilkan tunas serta akar baru dari ruasnya. Tumbuhan rimpang yang sering kita jumpai antara lain Temu Giring, Kunyit, Temu Ireng, Temulawak, Jahe Gajah, Jahe Merah, Jahe Emprit, Lempuyang, Bangle, Lengkuas dan Kencur. Rimpang menyimpan minyak  atsiri  dan  alkaloid dalam jumlah yang banyak, dimana kandungan ini dapat berkhasiat dalam bidang pengobatan (Feberian & Fitriati, 2022).")
   st.write("Secara umum idenifikasi pada jenis rimpang ini dapat dilakukan secara kasat mata, namun sayangnya masih banyak dari masyarakat kita yang sulit dan bingung dalam membedakan jenis rimpang, karena memiliki bentuk dan ciri yang mirip satu sama lain (Feberian & Fitriati, 2022) (Mawaddah et al., 2022). Hal ini yang menjadi dasar banyaknya peneliti yang mengeksplorasi metode baru guna malakukan klasifikasi rimpang secara otomatis dan efektif. Metode tersebut biasanya didasarkan pada fitur warna, bentuk dan tekstur.")

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("pages.klasifikasi.py", "Klasifikasi", "🖥️"),
    ]
)