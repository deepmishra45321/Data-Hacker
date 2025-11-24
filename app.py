"""
Data Hunting - End-to-End Machine Learning & Deep Learning Pipeline
Main application entry point
"""
import streamlit as st

# Import configuration
from config.settings import APP_TITLE, APP_ICON, LAYOUT, INITIAL_SIDEBAR_STATE

# Import core functionality
from core.session import initialize_session_state

# Import UI components
from ui import render_header, render_sidebar

# Import page modules
from pages import (
    render_home_page,
    render_preprocessing_page,
    render_eda_page,
    render_ml_training_page,
    render_dl_training_page,
    render_prediction_page,
    render_report_page,
    render_about_page
)


# Page Configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE
)

# Initialize Session State
initialize_session_state()

# Render Header
render_header()

# Render Sidebar Navigation
page = render_sidebar()

# Route to appropriate page
if page == "Home":
    render_home_page()
elif page == "Preprocessing":
    render_preprocessing_page()
elif page == "EDA":
    render_eda_page()
elif page == "ML Training":
    render_ml_training_page()
elif page == "DL Training":
    render_dl_training_page()
elif page == "Prediction":
    render_prediction_page()
elif page == "Report":
    render_report_page()
elif page == "About":
    render_about_page()
