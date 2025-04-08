import streamlit as st
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
st.sidebar.page_link("pages/Research.py", label="🧠 Research")



##############




st.markdown('<h1 style="color: Black; font-size: 50px; font-weight: bold;">Research</h1>', unsafe_allow_html=True)
st.markdown("Sección con distintos proyectos de investigación. Incluye descripción, enlace a repositorios públicos y ejemplos de código.", unsafe_allow_html=True)

# ----------------------
# Volatilidad Implícita
# ----------------------
st.markdown("---")
st.markdown("### 📊 Volatilidad Implícita")
st.markdown("Análisis y visualización de superficies de volatilidad en commodities agrícolas.")
st.markdown("[🔗 Ver repositorio en GitHub](https://github.com/juancassinerio/volatilidad-implicita)")

st.code("""
import numpy as np
import matplotlib.pyplot as plt

K = np.linspace(100, 200, 100)
vol = 0.3 * np.sqrt(0.5)
plt.plot(K, vol * np.ones_like(K))
plt.title("Curva de Volatilidad Implícita")
plt.show()
""", language="python")

# ----------------------
# Bonos y TIR
# ----------------------
st.markdown("---")
st.markdown("### 💰 Bonos y Tasa Interna de Retorno (TIR)")
st.markdown("Calculadora de precios de bonos y estimador de TIR con optimización.")
st.markdown("[🔗 Ver repositorio en GitHub](https://github.com/juancassinerio/bonos-tir)")

st.code("""
def bond_price(face, coupon, years, rate):
    return sum([(face * coupon) / (1 + rate)**t for t in range(1, years + 1)]) + face / (1 + rate)**years
""", language="python")

# ----------------------
# Estrategias Cuantitativas
# ----------------------
st.markdown("---")
st.markdown("### 🤖 Estrategias Cuantitativas")
st.markdown("Backtesting de estrategias de momentum, media móvil y mean-reversion.")
st.markdown("[🔗 Ver repositorio en GitHub](https://github.com/juancassinerio/estrategias-cuantitativas)")

st.code("""
import pandas as pd

def moving_average_strategy(prices):
    short_ma = prices.rolling(20).mean()
    long_ma = prices.rolling(50).mean()
    return (short_ma > long_ma).astype(int)
""", language="python")
