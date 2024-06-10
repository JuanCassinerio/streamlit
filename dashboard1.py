import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
from datetime import date
import requests 


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
data.drop_duplicates


today = date.today()
start_date = "2024-01-01"
start_date_date = pd.to_datetime(start_date).date()

filtered_df = data[data['fecha'].dt.date >= start_date_date]
filtered_df = filtered_df[filtered_df['fecha'].dt.date <= today]


#2-Selleccionar dolar
'''
blue                     
mayorista                
oficial                  
contadoconliqui           
bolsa                  
tarjeta                  
cripto      
'''

dolar='cripto' #selleccionar ACA de la lista

fig = px.line(filtered_df, x='fecha', y=dolar)
fig.update_layout(title=dict(text=f'Dolar {dolar} ',x=0.5,xanchor='center',font=dict(color="blue", size=14)))
fig.show()

#GUI
st.title("Tablero Empresas")
st.dataframe(vtiger)







