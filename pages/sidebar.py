# sidebar.py
import streamlit as st

def render_sidebar():
    st.markdown("""
        <style>
            [data-testid="stSidebarNavItems"] {
                display: none !important;
            }
            [data-testid="stSidebarNav"] > div:nth-child(1) {
                padding-top: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("# Navegación")
    st.sidebar.page_link("dashboard1.py", label="🏠 Inicio")
    st.sidebar.page_link("pages/portfolio.py", label="💰 Mi Portfolio")
    st.sidebar.page_link("pages/dolar.py", label="💲 Dolar Hoy")

    st.sidebar.markdown(" ")
    st.sidebar.page_link("pages/data.py", label="💸 Acciones y Cedears")


    st.sidebar.markdown("---")
    st.sidebar.markdown("## Más")
    st.sidebar.page_link("pages/contact.py", label="📞 Contacto")
    st.sidebar.page_link("pages/Research.py", label="🧠 Research")
