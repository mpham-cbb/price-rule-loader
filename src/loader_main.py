import sys
from pathlib import Path
import streamlit as st


try:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
except:
    pass

# import views
from view.home import homepage
from view.price_loader import price_loader
from view.contact import contact
from view.auth import require_login, auth_sidebar

# this is the visual shown in the broswer tab
st.set_page_config(page_title="New Price Rule Loader", layout="wide")

# Check authentication first
require_login()

# Set up sidebar with authentication info
st.sidebar.title("Navigation")

# Simple navigation options
nav_options = ["🏠 Home", "📂 Price Rule Loader", "📩 Contact"]
add_sidebar = st.sidebar.radio("Go to", nav_options)

# Display authentication info in sidebar
auth_sidebar()


# page render
if __name__ == "__main__":
    if add_sidebar == "🏠 Home":
        homepage()
    elif add_sidebar == "📂 Price Rule Loader":
        price_loader()
    elif add_sidebar == "📩 Contact":
        contact()

hide_streamlit_style = """
    <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)