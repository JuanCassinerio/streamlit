import streamlit as st
from yfinance import Ticker
import warnings
from datetime import datetime
from datetime import date
import plotly.graph_objects as go

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

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
st.sidebar.page_link("pages/portfolio.py", label="💰 Mi Portfolio")
st.sidebar.page_link("pages/dolar.py", label="💲 Dolar Hoy")
st.sidebar.markdown(" ")
st.sidebar.page_link("pages/data.py", label="💸 Acciones y Cedears")
st.sidebar.page_link("pages/data.py", label="🧾 Bonos")
st.sidebar.page_link("pages/data.py", label="🪙 Crypto")



st.sidebar.markdown("---")  # Optional horizontal line separator

st.sidebar.markdown("## Más")
st.sidebar.page_link("pages/contact.py", label="📞 Contacto")
st.sidebar.page_link("pages/Research.py", label="🧠 Research")

##############

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
    # Create a Plotly figure
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data['Close'])])
    fig.update_layout(title='AAPL Stock Price', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)  # Display the chart
else:
    st.write("No data available for the selected date range.")