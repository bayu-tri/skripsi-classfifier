from st_pages import Page, show_pages
import streamlit as st
from libs import *

# Optional -- adds the title and icon to the current page
# st.subheader(":gray[Tugas Akhir]")
st.header('KLASIFIKASI RIMPANG MENGGUNAKAN METODE CONVOLUTIONAL NEURAL NETWORK ARSITEKTUR MOBILENETV2', divider='rainbow')
# st.caption("Bayu Tri Nugroho (123190015)")

tab1, tab2, tab3 = st.tabs(["Abstrak", "Rumusan Masalah", "Tujuan Penelitian"])

with tab1:
   st.write("-")

with tab2:
   st.write("-")

with tab3:
   st.write("-")

show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("pages.klasifikasi.py", "Klasifikasi", "🖥️"),
    ]
)