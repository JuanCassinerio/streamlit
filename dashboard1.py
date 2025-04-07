import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

# streamlit run "C:/Users/Usuario/Desktop/Scripts/Nueva carpeta/dark box/st.py" ""to deal with folders with spaces

from functions import dolar

#GUI
import streamlit as st

st.set_page_config(page_title="Dolar Ya", page_icon="💸", layout="centered")

st.sidebar.markdown("# Navegación")
st.sidebar.page_link("dashboard1.py", label="🏠 Inicio")

st.sidebar.page_link("pages/data.py", label="🧪 Otro análisis")

st.markdown('''<h1 style="color: green; font-size: 50px; font-weight: bold;">Dolar Ya</h1>''',unsafe_allow_html=True)
st.markdown("Cotización en vivo e histórica (Fuentes: dolarapi.com / argentinadatos.com)", unsafe_allow_html=True)


st.sidebar.markdown("# Main page 🎈")

