import streamlit as st
import pandas as pd
import plotly.express as px
  # streamlit run "C:/Users/Usuario/Desktop/Scripts/Nueva carpeta/dark box/st.py" ""to deal with folders with spaces
from datetime import date, timedelta


from functions import dolar
#GUI
st.markdown('''<h1 style="color: grey; font-size: 50px; font-weight: bold;">Dolar Yaaaaa</h1>''',unsafe_allow_html=True)
st.markdown("Cotizacion en vivo e historica del dolar. Fuentes: dolarapi.com / argentinadatos.com", unsafe_allow_html=True)
#st.markdown("Para mas informacion ir a <a href='https://juancassinerio.wixsite.com/finance'>https://juancassinerio.wixsite.com/finance/</a>", unsafe_allow_html=True)


start_date0 = pd.to_datetime("2024-01-03").date()
end_date=date.today()
start_date1 = end_date - timedelta(days=30 * 3)  #4 months


new_start_date, new_end_date = st.slider("Fecha",start_date0, end_date,  (start_date1, end_date))

opciones_dolar = {
    "blue": "Blue",
    "mayorista": "Mayorista",
    "oficial": "Oficial",
    "contadoconliqui": "CCL",
    "bolsa": "Bolsa",
    "tarjeta": "Tarjeta",
    "cripto": "Cripto"
}

# Crear el radio button utilizando los nuevos nombres
chosen = st.radio("Seleccionar Dolar", tuple(opciones_dolar.values()), horizontal=True, key="sorting_hat_radio")

# Obtener el valor original (clave) a partir del valor seleccionado (valor)
chosen_key = [clave for clave, valor in opciones_dolar.items() if valor == chosen][0]

with st.spinner("Fetching data..."):
    dolar = dolar(new_start_date, new_end_date)
  
fig = px.line(dolar, x='fecha', y=chosen_key)
fig.update_layout(
    title=dict(
        text=f'Dolar {chosen} - {new_start_date}/{new_end_date}', 
        x=0.5, 
        xanchor='center', 
        font=dict(color="black", size=14)
    ),
    yaxis_title=None,  # Setting the y-axis title as [$]
    xaxis_title=None,  # Removing x-axis title
)

# Rotating the y-axis title horizontally (by setting angle to 0)
fig.update_yaxes(
    tickformat="$",  # Add the dollar symbol to labels
      # Alternatively, add the symbol as a suffix
)

st.plotly_chart(fig)

