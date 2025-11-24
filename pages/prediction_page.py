"""
Prediction page - Model prediction interface.
"""
import pandas as pd
import streamlit as st

def render_prediction_page():
    """Renders the prediction page with input form for predictions."""
    from features.prediction import make_prediction, get_prediction_probability

    st.markdown("### 🎲 Prediction Playground")
    
    if st.session_state['best_model'] is None:
        st.warning("Please train a model in 'ML Training' or 'DL Training' first.")
    elif st.session_state['cleaned_data'] is None:
        st.warning("Please process data first.")
    else:
        model = st.session_state['best_model']
        data = st.session_state['cleaned_data']
        X_train = data['X_train']
        
        st.markdown("#### Enter Input Values")
        
        # Dynamic Input Generation
        input_data = {}
        cols = X_train.columns.tolist()
        
        # Create 3 columns for inputs to save space
        col_list = st.columns(3)
        
        for i, col in enumerate(cols):
            with col_list[i % 3]:
                val = st.number_input(f"{col}", value=0.0)
                input_data[col] = val
                
        if st.button("🔮 Predict"):
            input_df = pd.DataFrame([input_data])
            
            try:
                prediction = make_prediction(model, input_df)
                
                st.success("Prediction Successful!")
                st.markdown(f"### Result: **{prediction[0]}**")
                
                if data['problem_type'] == "Classification":
                    # Try to get probability if available
                    proba = get_prediction_probability(model, input_df)
                    if proba is not None:
                        st.info(f"Probability: {proba[0]}")
                        
            except Exception as e:
                st.error(f"Prediction Error: {e}")
