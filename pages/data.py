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

# --- Time Range Setup ---
start_date0 = pd.to_datetime("2024-01-03").date()
end_date = date.today()
start_date1 = end_date - timedelta(days=30 * 3)

# --- Layout: Slider on left, Ticker input on right ---
col1, col2 = st.columns([3, 1])

with col2:
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN', '^GSPC']
    selected_ticker = st.selectbox("Ticker", tickers)
    custom_ticker = st.text_input("...o escribir uno", "")
    # Fallback logic

with col1:
    new_start_date, new_end_date = st.slider(
        "Seleccionar rango de fechas",
        min_value=start_date0,
        max_value=end_date,
        value=(start_date1, end_date),
        format="YYYY-MM-DD"
    )

    ticker = custom_ticker.upper() if custom_ticker else selected_ticker

    # --- Fetch Data ---
    data = price(ticker, new_start_date, new_end_date)

    # --- Plot ---
    if data is not None and not data.empty:

        fig = go.Figure(data=[go.Scatter(x=data['Date'], y=data['Adj Close'], name=ticker)])
        fig.update_layout(
            title=f'{ticker} Stock Price',
            xaxis_title='Date',
            yaxis_title='Price',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("⚠️ No data available for the selected date range or ticker.")

