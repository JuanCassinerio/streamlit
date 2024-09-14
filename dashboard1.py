import streamlit as st
import pandas as pd
import plotly.express as px
import requests  # streamlit run "C:/Users/Usuario/Desktop/Scripts/Nueva carpeta/dark box/st.py" ""to deal with folders with spaces
from datetime import date, timedelta

def dolar(start_date_date, end_date):
  url="https://api.argentinadatos.com/v1/cotizaciones/dolares"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
  data = requests.get(url, headers=headers, verify=False).json()
  data = pd.DataFrame.from_dict(data)
  data['precio'] = (data['compra']+data['venta'])/2
  data = data[['fecha','precio','casa']]
  casa_values = data['casa'].unique()  # Get unique casa values
  for casa in casa_values:
    data[f'{casa}'] = data[data['casa'] == casa]['precio']
  data.drop(['casa','precio','solidario'], axis=1, inplace=True)
  def fill_missing_by_fecha(df):
    return pd.concat([df[['fecha']], df.groupby('fecha').transform(lambda x: x.fillna(method='ffill'))], axis=1)
  data1 = fill_missing_by_fecha(data.copy())  # Avoid modifying original data
  data1.sort_index(ascending=False, inplace=True)  # Sort DataFrame by index in descending order
  data1.drop_duplicates(subset='fecha', keep='first', inplace=True)  # Keep the first occurrence of each unique 'fecha'
  data1.sort_index(ascending=True, inplace=True)  # Sort DataFrame by index in ascending order again
  
  url="https://dolarapi.com/v1/dolares"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
  data = requests.get(url, headers=headers, verify=False).json()
  data = pd.DataFrame.from_dict(data)
  data['precio'] = (data['compra']+data['venta'])/2
  data = data[['fechaActualizacion','precio','casa']]
  casa_values = data['casa'].unique()  # Get unique casa values
  for casa in casa_values:
    data[f'{casa}'] = data[data['casa'] == casa]['precio']
  data.drop(['casa','precio'], axis=1, inplace=True)
  def fill_missing_by_fecha(df):
    return pd.concat([df[['fechaActualizacion']], df.groupby('fechaActualizacion').transform(lambda x: x.fillna(method='ffill'))], axis=1)
  data2 = fill_missing_by_fecha(data.copy())  # Avoid modifying original data
  data2.sort_index(ascending=False, inplace=True)  # Sort DataFrame by index in descending order
  data2.drop_duplicates(subset='fechaActualizacion', keep='first', inplace=True)  # Keep the first occurrence of each unique 'fecha'
  data2.sort_index(ascending=True, inplace=True)  # Sort DataFrame by index in ascending order again
  data2['fechaActualizacion'] = pd.to_datetime(data['fechaActualizacion'])  # Convert to datetime if not already
  data2['fechaActualizacion'] -= pd.Timedelta(hours=1)
  data2 = data2.rename(columns={'fechaActualizacion': 'fecha'})
  data2['fecha'] = pd.to_datetime(data2['fecha']).dt.strftime('%Y-%m-%d')
  
  data = pd.concat([data1, data2], ignore_index=True)
  data['fecha'] = pd.to_datetime(data['fecha'])
  
  
  
  filtered_df = data[data['fecha'].dt.date >= start_date_date]
  filtered_df = filtered_df[filtered_df['fecha'].dt.date <= end_date]
  return filtered_df

#GUI
st.markdown('''<h1 style="color: grey; font-size: 50px; font-weight: bold;">Dolar Ya</h1>''',unsafe_allow_html=True)
st.markdown("Cotizacion en vivo e historica del dolar. Fuentes: dolarapi.com / argentinadatos.com", unsafe_allow_html=True)
st.markdown("Para mas informacion ir a <a href='https://juancassinerio.wixsite.com/finance'>https://juancassinerio.wixsite.com/finance/</a>", unsafe_allow_html=True)


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
    yaxis=dict(
        title="[$]",  # Setting the y-axis title as [$]
        title_standoff=20,  # Adjusts the distance between the title and the axis
        titlefont=dict(size=12),  # Set font size for better visibility
        tickprefix='$',  # Add a $ prefix to the y-axis values
    ),
    xaxis_title=None,  # Removing x-axis title
)

# Rotating the y-axis title horizontally (by setting angle to 0)
fig.update_yaxes(title_text="[$]", title_font=dict(size=14), title_angle=0)
st.plotly_chart(fig)

