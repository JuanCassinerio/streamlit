# GUI
import streamlit as st

st.set_page_config(page_title="Bursatil_Info", page_icon="📈", layout="wide")


#Navegacion
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


