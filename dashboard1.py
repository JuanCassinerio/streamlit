'''
streamlit run C:/Users/Usuario/Desktop/dashboard1.py
'''

import streamlit as st
from yfinance import Ticker  # Import yfinance for fetching data
import warnings

from datetime import datetime
from datetime import date
from collections.abc import Iterable

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # Rest of your Streamlit app code


# Function to fetch AAPL data from Yahoo Finance for a specific date range
def fetch_aapl_data(start_date, end_date):
  aapl = Ticker("AAPL")  # Create a Ticker object for AAPL
  # Download historical data (adjust period as needed)
  data = aapl.history(start=start_date, end=end_date)
  return data

# Initial date range (you can customize these)
today = date.today().strftime("%Y-%m-%d")

# Initial date range (you can customize these)
start_date = "2024-01-01"
end_date = today

# Create a sidebar for user input
st.sidebar.title("Date Filter")
date_format = "%Y-%m-%d"  # Adjust format if needed
start_date_obj = datetime.strptime(start_date, date_format)
end_date_obj = datetime.strptime(end_date, date_format)
new_start_date = st.sidebar.date_input("Start Date", value=start_date_obj)
new_end_date = st.sidebar.date_input("End Date", value=end_date_obj)


data = None  # Initialize data as None
# Button to apply changes and refetch data
if st.sidebar.button("Apply deherChanges"):
  # Update data based on user input
  start_date = new_start_date
  end_date = new_end_date
  data = fetch_aapl_data(start_date, end_date)  # Refetch data

# Display the title and descriptive text
st.title("My Online Dashboard")
st.write("This dashboard displays information about Apple (AAPL) stock.")


# Display the fetched data (assuming data is a pandas DataFrame)
if data is not None:
  st.dataframe(data)
else:
  st.write("No data available for the selected date range.")

# Button to refresh data (optional)
if st.button("Refresh Data"):
  data = fetch_aapl_data(start_date, end_date)  # Refetch data






