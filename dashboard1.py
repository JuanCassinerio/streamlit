import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
import requests 


#GUI
st.title("Cotizacion de los diferentes dolares a tiempo real",color=blue)
st.markdown("<p style='text-align: center;'>Para mas informacion ir a <a href='https://juancassinerio.wixsite.com/finance'>https://juancassinerio.wixsite.com/finance/</a>. Desarrollo de Algoritmos financieros. Procesamiento y Desarrollo de modelos econometricos</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Fuentes: <a href='https://dolarapi.com'>https://dolarapi.com/</a> y <a href='https://argentinadatos.com/'>https://argentinadatos.com/</a></p>", unsafe_allow_html=True)





