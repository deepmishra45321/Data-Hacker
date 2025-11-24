"""
Dynamic plotting functionality using Plotly.
"""
import plotly.express as px
import streamlit as st


def render_plot(df, plot_type, x_axis, y_axis, color_col):
    """
    Renders the selected plot using Plotly Express.
    
    Args:
        df: Input dataframe
        plot_type: Type of plot (Scatter, Line, Histogram, Box)
        x_axis: Column name for x-axis
        y_axis: Column name for y-axis
        color_col: Column name for color grouping
    """
    fig = None
    try:
        if plot_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col)
        elif plot_type == "Line Plot":
            fig = px.line(df, x=x_axis, y=y_axis, color=color_col)
        elif plot_type == "Histogram":
            fig = px.histogram(df, x=x_axis, color=color_col)
        elif plot_type == "Box Plot":
            fig = px.box(df, x=x_axis, y=y_axis, color=color_col)
        
        if fig:
            st.plotly_chart(fig, use_container_width=True)
            
    except Exception as e:
        st.error(f"Error rendering plot: {e}")
