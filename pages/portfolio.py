'''import streamlit as st
#Navegacion
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Agrega el directorio raíz al path

from pages.sidebar import render_sidebar
render_sidebar()

##############

st.markdown('<h1 style="color: Black; font-size: 50px; font-weight: bold;">Mi Portfolio</h1>', unsafe_allow_html=True)
st.markdown("En Construccion", unsafe_allow_html=True)
'''
import streamlit as st

'''st.set_page_config(page_title="Frutiger Aero App", layout="wide")

# Custom CSS for Frutiger Aero style
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #87CEEB, #4682B4); /* Blue gradient background */
        color: white;
        font-family: sans-serif;
    }

    .stApp {
        background: transparent; /* Make Streamlit app background transparent */
    }

    .st-emotion-cache-16txtl3 { /* Main container */
        background: rgba(255, 255, 255, 0.1); /* Glass effect background */
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Shadow for depth */
        backdrop-filter: blur(10px); /* Blur for glass effect */
    }

    .stButton>button {
        background: linear-gradient(to bottom, #87CEEB, #4682B4); /* Blue gradient button */
        color: white;
        border: none;
        border-radius: 20px;
        padding: 15px 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Shadow for depth */
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* Text shadow */
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(to bottom, #4682B4, #87CEEB); /* Reverse gradient on hover */
    }

    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div>input {
        background: rgba(255, 255, 255, 0.2); /* Slightly transparent input background */
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 10px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus, .stSelectbox>div>div>div>input:focus {
        border-color: #87CEEB;
        box-shadow: 0 0 5px rgba(135, 206, 235, 0.5);
    }

    .bubble-image { /* Style for the circular image */
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background: url('https://placekitten.com/200/200'); /* Replace with your image URL */
        background-size: cover;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        margin: 20px auto; /* Center the image */
    }

    .search-bar { /* Style for the search bar */
        background: rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 10px;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }

    .search-bar input[type="text"] {
        background: transparent;
        border: none;
        color: white;
        flex-grow: 1;
        padding: 5px;
    }

    .search-bar button {
        background: rgba(255, 255, 255, 0.3);
        border: none;
        border-radius: 20px;
        padding: 8px 15px;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Content of the app
st.title("Frutiger Aero App")

st.markdown("Experience the awesome Frutiger Aero aesthetic!")

st.markdown("<div class='search-bar'><input type='text' placeholder='Search...' /><button>Search</button></div>", unsafe_allow_html=True)

st.markdown("<div class='bubble-image'></div>", unsafe_allow_html=True)

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, step=1)
if st.button("Submit"):
    st.write(f"Name: {name}, Age: {age}")

st.markdown("Download the Frutiger Aero Pack:")
st.button("Download Pack")
'''

st.markdown("""
    <style>
    /* Apply a glassy background to the main content */
    .main {
        background: rgba(10, 15, 28, 0.8);
        backdrop-filter: blur(8px);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 0 20px #00ccff55;
    }

    /* Button style */
    .stButton > button {
        background: linear-gradient(145deg, #00ccff, #00ffcc);
        color: black;
        border-radius: 12px;
        border: none;
    }

    /* Make headings glow slightly */
    h1, h2, h3, h4 {
        text-shadow: 0 0 8px #00ccff;
    }
    </style>
""", unsafe_allow_html=True)