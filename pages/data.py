import streamlit as st


from datetime import timedelta
from datetime import date
import plotly.graph_objects as go


import pandas as pd



from functions import price
#Navegacion
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Agrega el directorio raíz al path

from pages.sidebar import render_sidebar

render_sidebar()

##############


# --- Ticker Input ---
tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']
selected_ticker = st.selectbox("Seleccionar ticker", tickers)
custom_ticker = st.text_input("...o escribir uno", "")

# Use the custom ticker if provided
ticker = custom_ticker.upper() if custom_ticker else selected_ticker

# --- Time Range Slider ---
start_date0 = pd.to_datetime("2024-01-03").date()
end_date = date.today()
start_date1 = end_date - timedelta(days=30 * 3)

new_start_date, new_end_date = st.slider(
    "Seleccionar rango de fechas",
    min_value=start_date0,
    max_value=end_date,
    value=(start_date1, end_date),
    format="YYYY-MM-DD"
)

# --- Fetch & Plot Data ---
data = price(ticker, new_start_date, new_end_date)

if data is not None and not data.empty:
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data['Close'], name=ticker)])
    fig.update_layout(title=f'{ticker} Stock Price', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)
else:
    st.write("No data available for the selected date range.")