# GUI
import streamlit as st

st.set_page_config(page_title="Bursatil_Info", page_icon="📈", layout="wide")
# Estilo CSS personalizado
st.markdown("""
    <style>
        .title-style {
            font-size: 48px;
            font-weight: 800;
            color: #0033cc;
        }
        .subtitle-style {
            font-size: 20px;
            color: #333333;
        }
        .highlight {
            color: #ffa500;
        }
        .info-box {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

#Navegacion
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Agrega el directorio raíz al path

from pages.sidebar import render_sidebar
render_sidebar()
##############

st.markdown('''
    <h1 style="font-size: 50px; font-weight: bold;">
        <span style="color: blue;">Bursatil</span>
        <span style="color: orange;">Info</span>
    </h1>
''', unsafe_allow_html=True)

st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <h3 style="font-size: 20px; margin-right: 5px;">
            Bienvenido a Bursatil Info – Tu espacio para explorar el mundo de las inversiones de forma clara y accesible.
            Acá vas a poder gestionar tu portafolio, seguir la cotización del dólar en tiempo real y analizar proyecciones de acciones y CEDEARs. Todo desde un solo lugar, con herramientas pensadas para vos.
        </h3>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <h3 style="color: black; font-size: 15px; font-weight: bold; margin-right: 5px;">
            Hecho por Juan Cassinerio - Para más información ir a 
            <a href='https://juancassinerio.wixsite.com/finance' target='_blank'>
                juancassinerio.wixsite.com/finance
            </a>
        </h3>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("---")
st.write("### Navegación")

col1, col2, col3 = st.columns([1, 1, 1])


with col1:
    if st.button("📊 Mi Portafolio"):
        st.switch_page("pages/data.py")
    st.markdown("Conoce el rendimiento de tus inveriones, Defini Tu cartera y conoce tu rendimiento Anual Global",
                unsafe_allow_html=True)

with col2:
    if st.button("💸 Dolar Hoy"):
        st.switch_page("pages/dolar.py")
    st.markdown("Cotización en Vivo e Histórica de TODOS los Dolares",
                unsafe_allow_html=True)

with col3:
    if st.button("🧪 Acciones Proyeciones"):
        st.switch_page("pages/dolar.py")
    st.markdown("Analisis Fundamental y Tecnico de Acciones y Cedears",
                unsafe_allow_html=True)


