"""
Data loading and snapshot functionality.
"""
import pandas as pd
import streamlit as st


def load_data(uploaded_file):
    """
    Loads data from uploaded CSV or XLSX file.
    """
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None


def get_data_snapshot(df):
    """
    Returns a dictionary with data snapshot information.
    """
    snapshot = {
        'rows': df.shape[0],
        'columns': df.shape[1],
        'missing': df.isna().sum().sum(),
        'duplicates': df.duplicated().sum(),
        'numeric_cols': df.select_dtypes(include=['number']).shape[1],
        'categorical_cols': df.select_dtypes(include=['object', 'category']).shape[1]
    }
    return snapshot


def render_data_snapshot(snapshot):
    """
    Renders a visual snapshot of the data.
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Rows", snapshot['rows'])
        st.metric("Total Columns", snapshot['columns'])
        
    with col2:
        st.metric("Missing Values", snapshot['missing'])
        st.metric("Duplicates", snapshot['duplicates'])
        
    with col3:
        st.metric("Numeric Columns", snapshot['numeric_cols'])
        st.metric("Categorical Columns", snapshot['categorical_cols'])
