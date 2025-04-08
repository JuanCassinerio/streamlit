import streamlit as st
#Navegacion
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Agrega el directorio raíz al path

from pages.sidebar import render_sidebar
render_sidebar()

##############

st.markdown('<h1 style="color: Black; font-size: 50px; font-weight: bold;">Mi Portfolio</h1>', unsafe_allow_html=True)
st.markdown("En Construccion", unsafe_allow_html=True)

