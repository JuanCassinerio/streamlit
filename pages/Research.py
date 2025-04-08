#Navegacion
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
st.sidebar.page_link("pages/portfolio.py", label="💰 Mi Portfolio")
st.sidebar.page_link("pages/dolar.py", label="💲 Dolar Hoy")
st.sidebar.markdown(" ")
st.sidebar.page_link("pages/data.py", label="💸 Acciones y Cedears")
st.sidebar.page_link("pages/data.py", label="🧾 Bonos")
st.sidebar.page_link("pages/data.py", label="🪙 Crypto")



st.sidebar.markdown("---")  # Optional horizontal line separator

st.sidebar.markdown("## Más")
st.sidebar.page_link("pages/contact.py", label="📞 Contacto")
st.sidebar.page_link("pages/contact.py", label="🧠 Research")

##############