"""
Advanced visualizations: heatmap and pairplot using Seaborn.
"""
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def render_heatmap(df):
    """
    Renders a correlation heatmap using Seaborn.
    
    Args:
        df: Input dataframe
    """
    try:
        numeric_df = df.select_dtypes(include=['number'])
        if numeric_df.empty:
            st.warning("No numerical columns for heatmap.")
            return

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error rendering heatmap: {e}")


def render_pairplot(df, hue_col):
    """
    Renders a pairplot using Seaborn.
    
    Args:
        df: Input dataframe
        hue_col: Column name for hue grouping
    """
    try:
        if hue_col == "None":
            hue_col = None
            
        fig = sns.pairplot(df, hue=hue_col)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error rendering pairplot: {e}")
