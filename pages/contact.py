import streamlit as st
#Navegacion
from sidebar import render_sidebar
render_sidebar()
##############


st.markdown('<h1 style="color: Black; font-size: 50px; font-weight: bold;">Contacto</h1>', unsafe_allow_html=True)

# Crear dos columnas
col1, col2 = st.columns([1, 2])  # col1 más angosta para la imagen, col2 para el texto

with col1:
    import os


    image_path = os.path.join(os.path.dirname(__file__), "..", "images", "picture.jpg")
    with open(image_path, "rb") as img_file:
        st.image(img_file.read(), width=200)

with col2:
    st.markdown("""
    <h2 style="color: #333333;">Juan Cassinerio</h2>
    <p style="font-size: 18px;">
        Analista Cuantitativo<br>
        Físico y Magíster en Finanzas<br>
        Idóneo CNV
    </p>
    """, unsafe_allow_html=True)
