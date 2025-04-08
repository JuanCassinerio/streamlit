import streamlit as st
#Navegacion
from sidebar import render_sidebar
render_sidebar()



##############




st.markdown('<h1 style="color: Black; font-size: 50px; font-weight: bold;">Research</h1>', unsafe_allow_html=True)
st.markdown("Sección con distintos proyectos de investigación. Incluye descripción, enlace a repositorios públicos y ejemplos de código.", unsafe_allow_html=True)


# ----------------------
# Volatilidad Implícita
# ----------------------
st.markdown("---")
st.markdown("### 📊 Volatilidad Implícita")

st.markdown("Análisis y visualización de superficies de volatilidad en commodities agrícolas.")
st.markdown("[🔗 Ver repositorio en GitHub](https://github.com/juancassinerio)")

st.code("""
import numpy as np
import matplotlib.pyplot as plt

K = np.linspace(100, 200, 100)
vol = 0.3 * np.sqrt(0.5)
plt.plot(K, vol * np.ones_like(K))
plt.title("Curva de Volatilidad Implícita")
plt.show()
""", language="python")







