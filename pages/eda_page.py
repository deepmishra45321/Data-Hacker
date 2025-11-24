"""
EDA page - Exploratory data analysis interface.
"""
import streamlit as st

def render_eda_page():
    """Renders the EDA page with dynamic plotting and visualization tools."""
    from features.eda import render_plot, render_heatmap, render_pairplot

    st.markdown("### 📊 Exploratory Data Analysis")
    
    # Use cleaned data if available, else raw data
    if st.session_state['cleaned_data'] is not None:
        st.info("Using Processed Data for Analysis")
        df = st.session_state['data']
    elif st.session_state['data'] is not None:
        df = st.session_state['data']
    else:
        st.warning("Please upload data first.")
        df = None

    if df is not None:
        all_cols = df.columns.tolist()
        
        # 1. Dynamic Plotter
        st.markdown("#### 1. Dynamic Plotter")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            plot_type = st.selectbox("Select Plot Type", ["Scatter Plot", "Line Plot", "Histogram", "Box Plot"])
        with col2:
            x_axis = st.selectbox("X-Axis", all_cols)
        with col3:
            # Y-axis optional for Histogram
            if plot_type == "Histogram":
                y_axis = None
            else:
                y_axis = st.selectbox("Y-Axis", all_cols)
        with col4:
            color_col = st.selectbox("Color (Hue)", ["None"] + all_cols)
            if color_col == "None":
                color_col = None
        
        if st.button("Generate Plot"):
            render_plot(df, plot_type, x_axis, y_axis, color_col)
            
        # 2. Correlation Heatmap
        st.markdown("#### 2. Correlation Heatmap")
        if st.checkbox("Show Heatmap"):
            render_heatmap(df)
            
        # 3. Pairplot Generator
        st.markdown("#### 3. Pairplot Generator (Bonus)")
        pairplot_hue = st.selectbox("Pairplot Hue", ["None"] + all_cols)
        if st.button("Generate Pairplot"):
            with st.spinner("Generating Pairplot... this may take a moment."):
                render_pairplot(df, pairplot_hue)
