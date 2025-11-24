"""
Report page - Auto-generated report download interface.
"""
import streamlit as st
from core.data_loader import get_data_snapshot
from core.report import generate_report


def render_report_page():
    """Renders the report page with auto-generated session report."""
    st.markdown("### 📄 Auto-Generated Report")
    
    if st.session_state['data'] is None:
        st.warning("No data loaded.")
    else:
        snapshot = get_data_snapshot(st.session_state['data'])
        
        report_text = generate_report(
            snapshot, 
            st.session_state['cleaned_data'], 
            st.session_state['best_model']
        )
        
        st.text_area("Report Preview", report_text, height=400)
        
        st.download_button(
            label="📥 Download Report",
            data=report_text,
            file_name="Data_Hunting_Report.txt",
            mime="text/plain"
        )
