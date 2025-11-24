"""
Home page - Data loading interface.
"""
import streamlit as st
from core import data_loader


def render_home_page():
    """Renders the home page with data upload functionality."""
    st.markdown("### 📂 Data Loading")
    
    uploaded_file = st.file_uploader("Upload your dataset (CSV or XLSX)", type=['csv', 'xlsx'])
    
    if uploaded_file:
        df = data_loader.load_data(uploaded_file)
        
        if df is not None:
            st.session_state['data'] = df
            st.success(f"File '{uploaded_file.name}' loaded successfully!")
            
            # Data Snapshot
            snapshot = data_loader.get_data_snapshot(df)
            data_loader.render_data_snapshot(snapshot)
            
            # Preview
            with st.expander("👀 View Raw Data", expanded=True):
                st.dataframe(df.head())
