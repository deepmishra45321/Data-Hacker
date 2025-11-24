"""
Preprocessing page - Data cleaning and feature engineering interface.
"""
import streamlit as st

def render_preprocessing_page():
    """Renders the preprocessing page with data cleaning and engineering tools."""
    from features.preprocessing import (
        remove_duplicates,  
        handle_missing_values,
        drop_columns,
        get_column_types,
        encode_categorical,
        scale_features,
        split_dataset
    )

    st.markdown("### 🛠️ Data Preprocessing (The Cleaning Lab)")
    
    if st.session_state['data'] is None:
        st.warning("Please upload a dataset in the Home page first.")
    else:
        df = st.session_state['data'].copy()
        
        # 1. Duplicate Manager
        st.markdown("#### 1. Duplicate Manager")
        if st.button("Remove Duplicates"):
            df, removed = remove_duplicates(df)
            st.session_state['data'] = df
            st.success(f"Removed {removed} duplicate rows.")
            
        # 2. Missing Value Manager
        st.markdown("#### 2. Missing Value Manager")
        if st.button("Fill Missing Values"):
            df, filled_info = handle_missing_values(df)
            st.session_state['data'] = df
            
            if filled_info:
                st.success("Missing values filled successfully!")
                with st.expander("See Details"):
                    for col, info in filled_info.items():
                        st.write(f"**{col}** ({info['type']}): Filled {info['count']} missing values with '{info['value']}' (Method: {info['method']})")
            else:
                st.info("No missing values found in the dataset.")
                
        # 3. Column Manager
        st.markdown("#### 3. Column Manager")
        all_cols = df.columns.tolist()
        cols_to_drop = st.multiselect("Select columns to drop", all_cols)
        
        # 4. Target & Problem Type
        st.markdown("#### 4. Target & Problem Type")
        col1, col2 = st.columns(2)
        with col1:
            target_col = st.selectbox("Select Target Variable (y)", all_cols)
        with col2:
            problem_type = st.radio("Problem Type", ["Classification", "Regression"])
            
        # 5. Feature Engineering
        st.markdown("#### 5. Feature Engineering")
        
        # Encoding
        numeric_cols, cat_cols = get_column_types(df)
        encoding_method = "None"
        if cat_cols:
            st.info(f"Categorical Columns Detected: {cat_cols}")
            encoding_method = st.radio("Encoding Method", ["Label Encoding", "One-Hot Encoding"], horizontal=True)
        
        # Scaling
        scaling_method = st.radio("Scaling Method", ["None", "StandardScaler", "MinMaxScaler"], horizontal=True)
        
        # 6. Train-Test Split
        st.markdown("#### 6. Train-Test Split")
        test_size = st.slider("Test Size", 0.1, 0.5, 0.2)
        
        # Process Button
        if st.button("⚙️ Process & Save Data"):
            try:
                # Validate target column is not in drop list
                if target_col in cols_to_drop:
                    st.error(f"Error: Target column '{target_col}' cannot be dropped. Please remove it from the drop list.")
                else:
                    # Drop columns
                    df_clean = drop_columns(df, cols_to_drop)
                    
                    # Validate target column exists
                    if target_col not in df_clean.columns:
                        st.error(f"Error: Target column '{target_col}' not found in the dataset.")
                    else:
                        # Encode
                        if cat_cols:
                            df_clean, _ = encode_categorical(df_clean, encoding_method, cat_cols)
                        
                        # Scale
                        df_clean, _ = scale_features(df_clean, scaling_method, target_col)
                        
                        # Split
                        X_train, X_test, y_train, y_test = split_dataset(df_clean, target_col, test_size, problem_type)
                        
                        # Validate split results
                        if X_train is None or X_test is None:
                            st.error("Error: Failed to split the dataset. Please check your data and try again.")
                        else:
                            # Save to Session State
                            st.session_state['cleaned_data'] = {
                                'X_train': X_train,
                                'X_test': X_test,
                                'y_train': y_train,
                                'y_test': y_test,
                                'target_col': target_col,
                                'problem_type': problem_type
                            }
                            
                            st.success("Data processed and saved successfully! Go to 'EDA' or 'Model Training'.")
                            
                            with st.expander("View Processed Data Shapes"):
                                st.write(f"X_train: {X_train.shape}")
                                st.write(f"X_test: {X_test.shape}")
                    
            except Exception as e:
                st.error(f"An error occurred during processing: {e}")
