import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

# streamlit run "C:/Users/Usuario/Desktop/Scripts/Nueva carpeta/dark box/st.py" ""to deal with folders with spaces

from functions import dolar




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
st.sidebar.page_link("pages/data.py", label="🧪 Otro análisis")
st.sidebar.page_link("pages/dolar.py", label="💸 Dolar Hoy")
st.sidebar.page_link("pages/dolar.py", label="💸 Otra página")

st.sidebar.markdown("---")  # Optional horizontal line separator

st.sidebar.markdown("## Más")
st.sidebar.page_link("pages/contact.py", label="📬 Contacto")



st.markdown('<h1 style="color: green; font-size: 50px; font-weight: bold;">Dolar Ya</h1>', unsafe_allow_html=True)
st.markdown("Cotizacion en Hivo e Historica (Fuentes: dolarapi.com / argentinadatos.com)", unsafe_allow_html=True)









opciones_dolar = {"blue": "Blue","mayorista": "Mayorista","oficial": "Oficial","contadoconliqui": "CCL","bolsa": "Bolsa","tarjeta": "Tarjeta","cripto": "Cripto"}
chosen = st.radio("Seleccionar Dolar", tuple(opciones_dolar.values()), horizontal=True, key="sorting_hat_radio") #dolar type button
chosen_key = [clave for clave, valor in opciones_dolar.items() if valor == chosen][0]


start_date0 = pd.to_datetime("2024-01-03").date()
end_date=date.today()
start_date1 = end_date - timedelta(days=30 * 3)  #4 months
new_start_date, new_end_date = st.slider("Fecha",start_date0, end_date,  (start_date1, end_date)) #time slider

with st.spinner("Fetching data..."):
    dolar = dolar(new_start_date, new_end_date) #api data query

fig = px.line(dolar, x='fecha', y=chosen_key)
fig.update_layout(title=dict(
        text=f'Dolar {chosen} - {new_start_date}/{new_end_date}', x=0.5, xanchor='center',
        font=dict(color="black", size=14)),yaxis_title=None,xaxis_title=None,)
fig.update_yaxes(tickformat="$")

st.plotly_chart(fig)

