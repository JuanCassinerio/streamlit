import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
import requests  # streamlit run "C:/Users/Usuario/Desktop/Scripts/Nueva carpeta/dark box/st.py" ""to deal with folders with spaces

#GUI
st.markdown('''<h1 style="color: grey; font-size: 50px; font-weight: bold;">Dolar Ya</h1>''',unsafe_allow_html=True)
st.markdown("Cotizacion en vivo e historica del dolar. Fuentes: dolarapi.com / argentinadatos.com", unsafe_allow_html=True)
st.markdown("Para mas informacion ir a <a href='https://juancassinerio.wixsite.com/finance'>https://juancassinerio.wixsite.com/finance/</a>", unsafe_allow_html=True)


