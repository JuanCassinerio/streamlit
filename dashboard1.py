import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

# streamlit run "C:/Users/Usuario/Desktop/Scripts/Nueva carpeta/dark box/st.py" ""to deal with folders with spaces

from functions import dolar

#GUI
# Custom CSS for wider layout and background color
st.markdown("""
    <style>
        '''/* Make the app wider */
        .main {
            max-width: 90%;
            padding-left: 5%;
            padding-right: 5%;
        }'''

        /* Change background color */
        body {
            background-color: #ff2d00; /* light gray */
        }

        /* Optional: change sidebar background */
        .css-1d391kg {  /* Class may change on future Streamlit updates */
            background-color: #ff2d00 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('''<h1 style="color: grey; font-size: 50px; font-weight: bold;">Dolar Ya</h1>''',unsafe_allow_html=True)
st.markdown("Cotizacion en Hivo e Historica (Fuentes: dolarapi.com / argentinadatos.com)", unsafe_allow_html=True)

st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <h3 style="color: black; font-size: 15px; font-weight: bold; margin-right: 5px;">
            Hecho por Juan Cassinerio
        <span style="font-size: 15px;">
            Para más información ir a 
            <a href='https://juancassinerio.wixsite.com/finance' target='_blank'>
                juancassinerio.wixsite.com/finance
            </a>
        </span></h3>
        
    </div>
    """,
    unsafe_allow_html=True,
)







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

