import streamlit as st
from utils.auth_utils import check_authentication, logout_user, is_authenticated


def auth_sidebar():
    """Display authentication status in sidebar"""
    if is_authenticated():
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 👤 User Session")
        if st.sidebar.button("🚪 Logout"):
            logout_user()
            st.rerun()
    else:
        st.sidebar.markdown("---")
        st.sidebar.error("Not logged in")


def require_login():
    """Check if user is logged in, show login page if not"""
    check_authentication()
