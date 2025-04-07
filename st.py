import streamlit as st

st.set_page_config(page_title="Dolar Ya", page_icon="💸", layout="centered")

st.sidebar.markdown("# Navegación")
st.sidebar.page_link("st.py", label="🏠 Inicio")
st.sidebar.page_link("pages/dashbpard.py", label="📈 Histórico")
st.sidebar.page_link("pages/data.py", label="🧪 Otro análisis")

st.markdown('''<h1 style="color: green; font-size: 50px; font-weight: bold;">Dolar Ya</h1>''',unsafe_allow_html=True)
st.markdown("Cotización en vivo e histórica (Fuentes: dolarapi.com / argentinadatos.com)", unsafe_allow_html=True)
