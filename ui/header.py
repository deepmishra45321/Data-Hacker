"""
Header component for the application.
"""
import streamlit as st


def render_header():
    """
    Renders the main header of the application with a Netflix-style aesthetic.
    """
    st.markdown(
        """
        <style>
        .title-text {
            color: #E50914; /* Netflix Red */
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-weight: bold;
            font-size: 3rem;
            text-align: center;
            padding-bottom: 20px;
            text-shadow: 2px 2px 4px #000000;
        }
        .subtitle-text {
            color: #ffffff;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.2rem;
            text-align: center;
            margin-bottom: 30px;
        }
        </style>
        <div class="title-text">DATA HUNTING</div>
        <div class="subtitle-text">End-to-End Machine Learning & Deep Learning Pipeline</div>
        """,
        unsafe_allow_html=True
    )
