import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

# streamlit run "C:/Users/Usuario/Desktop/Scripts/Nueva carpeta/dark box/st.py" ""to deal with folders with spaces

from functions import dolar

#GUI
st.markdown('''<h1 style="color: grey; font-size: 50px; font-weight: bold;">Dolar Ya</h1>''',unsafe_allow_html=True)
st.markdown("Cotizacion en Hivo e Historica (Fuentes: dolarapi.com / argentinadatos.com)", unsafe_allow_html=True)
st.markdown('''
<h3 style="color: black; font-size: 15px; font-weight: bold;">
    Hecho por Juan Cassinerio
</h3>
<p>Para más información ir a 
    <a href='https://juancassinerio.wixsite.com/finance' target='_blank'>
        juancassinerio.wixsite.com/finance
    </a>
</p>
''', unsafe_allow_html=True)






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

