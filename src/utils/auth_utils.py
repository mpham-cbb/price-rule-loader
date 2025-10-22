import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_authentication():
    """Simple authentication system using environment variables"""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🔐 Authentication Required")
        st.markdown("Please enter your credentials to access the Price Rule Loader")
        
        # Get credentials from environment variables
        valid_username = os.getenv("PRICE_LOADER_USERNAME")
        valid_password = os.getenv("PRICE_LOADER_PASSWORD")
        
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button("Login")
            
            if submit_button:
                if username == valid_username and password == valid_password:
                    st.session_state.authenticated = True
                    st.success("✅ Authentication successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials. Please try again.")
                    st.markdown(
                        "<p style='font-size: 0.9em; color: gray;'>"
                        "If you continue to experience login issues, please contact Mia Pham at "
                        "<a href='mailto:nguyen.pham@cornerstone.com'>nguyen.pham@cornerstone.com</a>."
                        "</p>",
                        unsafe_allow_html=True,
                    )
        
        st.stop()

def logout_user():
    """Logout user and clear session state"""
    st.session_state.authenticated = False

def is_authenticated() -> bool:
    """Check if user is authenticated"""
    return st.session_state.get("authenticated", False)
