import streamlit as st
import mysql.connector
import pandas as pd
import datetime
import plotly.graph_objects as go  

#Coneccion y Fuente de Datos
hostname = "db-vtiger-tableau-ar.ca4cxchfpbn1.sa-east-1.rds.amazonaws.com" # vtiger prod(lectura)
username = "agdb"
password = "AGvtigerXLS"
database = "agrired-vtiger"
connection = mysql.connector.connect(host=hostname,user=username,password=password,database=database)
cursor = connection.cursor()

query = "SELECT * FROM `agrired-vtiger`.`vtiger_account`;"
cursor.execute(query)
rows = cursor.fetchall()
vtiger = pd.DataFrame(rows, columns=[i[0] for i in cursor.description]) 

#Procesamiento de Datos



#GUI
st.title("Tablero Empresas")
st.dataframe(vtiger)

cursor.close()
connection.close()





