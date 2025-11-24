"""
Session state management for the application.
"""
import streamlit as st


def initialize_session_state():
    """
    Initializes all session state variables.
    """
    if 'data' not in st.session_state:
        st.session_state['data'] = None
    if 'cleaned_data' not in st.session_state:
        st.session_state['cleaned_data'] = None
    if 'best_model' not in st.session_state:
        st.session_state['best_model'] = None
