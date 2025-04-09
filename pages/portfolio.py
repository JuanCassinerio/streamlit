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

# Theme settings (as provided)
st.set_page_config(page_title="Frutiger Aero Inspired App", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #0f1117;
        color: #ffffff;
        font-family: sans-serif;
    }

    .stApp {
        background-color: #0f1117;
    }

    .st-emotion-cache-16txtl3 { /* Main container */
        background-color: #262730;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Adding a subtle shadow */
        background-image: linear-gradient(to bottom, #262730, #1a1b22); /* Subtle gradient for depth */
    }

    .stButton>button {
        background-color: #0033cc;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        background-color: #002299;
    }

    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div>input {
        background-color: #333333;
        color: white;
        border: 1px solid #555555;
        border-radius: 5px;
        padding: 8px;
    }

    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus, .stSelectbox>div>div>div>input:focus {
        border-color: #0033cc;
        box-shadow: 0 0 5px rgba(0, 51, 204, 0.5);
    }

    /* Add a subtle glass effect to elements */
    .glass-effect {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .st-emotion-cache-10trblm{
        background-color: rgba(255, 255, 255, 0.05); /* very light semi transparent white*/
        border-radius: 5px;
        padding: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Add a subtle inner shadow to input elements */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div>input{
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Example content
st.title("Frutiger Aero Inspired Interface")

st.markdown("Welcome to the futuristic interface!")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, step=1)
option = st.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])

if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Selected option: {option}")

st.markdown("---")

st.markdown("Some more content with a subtle glass effect:")
st.markdown("<div class='glass-effect'>This is a glass-effect element.</div>", unsafe_allow_html=True)

st.markdown("More stylized sections")
st.markdown("<div class='st-emotion-cache-10trblm'> This is a section with a slightly different background</div>", unsafe_allow_html=True)