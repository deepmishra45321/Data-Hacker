"""
ML Training page - Machine learning model training interface.
"""
import streamlit as st

def render_ml_training_page():
    """Renders the ML training page with model selection and training tools."""
    from features.ml_training import train_model, evaluate_model, compare_all_models

    st.markdown("### ⚔️ ML Model Training (The Arena)")
    
    if st.session_state['cleaned_data'] is None:
        st.warning("Please process your data in the 'Preprocessing' page first.")
    else:
        data = st.session_state['cleaned_data']
        X_train = data['X_train']
        X_test = data['X_test']
        y_train = data['y_train']
        y_test = data['y_test']
        problem_type = data['problem_type']
        
        st.info(f"Problem Type: **{problem_type}**")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("#### Model Selection")
            if problem_type == "Classification":
                model_options = ["Logistic Regression", "Decision Tree", "Random Forest", "SVM", "KNN"]
            else:
                model_options = ["Linear Regression", "Decision Tree", "Random Forest", "SVR"]
                
            selected_model = st.selectbox("Choose Algorithm", model_options)
            
            # Hyperparameters
            params = {}
            st.markdown("#### Hyperparameters")
            
            if selected_model == "Random Forest":
                params['n_estimators'] = st.slider("n_estimators", 10, 200, 100)
                params['max_depth'] = st.slider("max_depth", 1, 20, 10)
            elif selected_model == "Decision Tree":
                params['max_depth'] = st.slider("max_depth", 1, 20, 10)
            elif selected_model == "SVM" or selected_model == "SVR":
                params['C'] = st.number_input("C (Regularization)", 0.01, 10.0, 1.0)
                params['kernel'] = st.selectbox("Kernel", ['linear', 'poly', 'rbf'])
            elif selected_model == "KNN":
                params['n_neighbors'] = st.slider("n_neighbors", 1, 20, 5)
            
            if st.button("🚀 Train Model"):
                with st.spinner("Training in progress..."):
                    try:
                        model = train_model(selected_model, problem_type, params, X_train, y_train)
                        metrics, fig = evaluate_model(model, X_test, y_test, problem_type)
                        
                        st.session_state['best_model'] = model
                        
                        st.success("Training Complete!")
                        st.markdown("#### Evaluation Metrics")
                        for k, v in metrics.items():
                            st.metric(k, f"{v:.4f}")
                            
                        st.markdown("#### Visualization")
                        st.pyplot(fig)
                        
                    except Exception as e:
                        st.error(f"Training failed: {e}")

        with col2:
            st.markdown("#### 🏆 Leaderboard (Bonus)")
            if st.button("Compare All Models"):
                with st.spinner("Comparing all models..."):
                    results_df, best_model, best_name = compare_all_models(X_train, X_test, y_train, y_test, problem_type)
                    st.dataframe(results_df.sort_values(by=results_df.columns[1], ascending=False))
                    
                    st.success(f"Best Model: **{best_name}**")
                    st.session_state['best_model'] = best_model
