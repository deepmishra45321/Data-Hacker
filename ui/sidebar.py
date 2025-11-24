"""
Sidebar navigation component.
"""
import streamlit as st


def render_sidebar():
    """
    Renders the sidebar navigation and returns the selected page.
    
    Returns:
        str: Selected page name
    """
    st.sidebar.markdown(
        """
        <style>
        .sidebar-header {
            color: #E50914;
            font-weight: bold;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        </style>
        <div class="sidebar-header">Navigation</div>
        """,
        unsafe_allow_html=True
    )
    
    page = st.sidebar.radio(
        "Go to",
        ["Home", "Preprocessing", "EDA", "ML Training", "DL Training", "Prediction", "Report", "About"],
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("Data Hunting v1.0")
    
    return page
