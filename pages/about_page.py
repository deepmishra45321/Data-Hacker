"""
About page - Application information and author details.
"""
import streamlit as st


def render_about_page():
    """Renders the about page with application and author information."""
    st.markdown("### 👨‍💻 About Me")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Profile picture
        st.image("assets/profile.jpg", width=150)
        
    with col2:
        st.markdown("""
        **Name:** Deepak Mishra  
        **Role:** B.Tech AIML Student (3rd Year)  
        
        **Bio:**  
        I am an aspiring AI Engineer. This 'Data Hunting' app is a generalized ML pipeline designed to democratize data science.
        
        **Connect with me:**
        - [LinkedIn](#)
        - [GitHub](#)
        """)
        
    st.markdown("---")
    st.info("Built with Streamlit, Pandas, Scikit-Learn, TensorFlow, and Plotly.")
