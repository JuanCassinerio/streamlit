# GUI
import streamlit as st

st.set_page_config(page_title="Dolar Ya", page_icon="💸", layout="centered")

st.sidebar.markdown("# Navegación")
st.sidebar.page_link("dashboard1.py", label="🏠 Inicio")
st.sidebar.page_link("pages/data.py", label="🧪 Otro análisis")
st.sidebar.page_link("pages/another_page.py", label="📊 Otra página")

st.markdown('''
    <h1 style="color: green; font-size: 50px; font-weight: bold;">Dolar Ya</h1>
''', unsafe_allow_html=True)

st.markdown("Cotización en vivo e histórica (Fuentes: dolarapi.com / argentinadatos.com)", unsafe_allow_html=True)




