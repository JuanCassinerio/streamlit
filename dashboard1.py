# GUI
import streamlit as st

st.set_page_config(page_title="Dolar Ya", page_icon="💸", layout="centered")
st.markdown("""
    <style>
        /* Hide default page navigation */
        [data-testid="stSidebarNavItems"] {
            display: none !important;
        }

        /* Optional: reduce padding where the nav was */
        [data-testid="stSidebarNav"] > div:nth-child(1) {
            padding-top: 0rem;
        }
    </style>
""", unsafe_allow_html=True)
st.sidebar.markdown("# Navegación")
st.sidebar.page_link("dashboard1.py", label="🏠 Inicio")
st.sidebar.page_link("pages/data.py", label="🧪 Otro análisis")
st.sidebar.page_link("pages/dolar.py", label="📊 Otra página")

st.markdown('''
    <h1 style="color: green; font-size: 50px; font-weight: bold;">Dolar Ya</h1>
''', unsafe_allow_html=True)

st.markdown("Cotización en vivo e histórica (Fuentes: dolarapi.com / argentinadatos.com)", unsafe_allow_html=True)


st.write("---")
st.write("### Navegación")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Inicio"):
        st.switch_page("dashboard1.py")

with col2:
    if st.button("🧪 Otro análisis"):
        st.switch_page("pages/data.py")

with col3:
    if st.button("📊 Otra página"):
        st.switch_page("pages/dolar.py")


