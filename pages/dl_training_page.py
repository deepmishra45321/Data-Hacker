"""
DL Training page - Deep learning model building interface.
"""
import streamlit as st

def render_dl_training_page():
    """Renders the DL training page with neural network configuration tools."""
    from features.dl_training import build_dl_model, compile_and_train

    st.markdown("### 🧠 Deep Learning Builder (The Neural Builder)")
    
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
            st.markdown("#### Network Architecture")
            num_layers = st.number_input("Number of Hidden Layers", 1, 10, 2)
            
            layers_config = []
            for i in range(int(num_layers)):
                st.markdown(f"**Layer {i+1}**")
                neurons = st.number_input(f"Neurons (L{i+1})", 1, 512, 64, key=f"n{i}")
                activation = st.selectbox(f"Activation (L{i+1})", ["relu", "sigmoid", "tanh", "softmax"], key=f"a{i}")
                dropout = st.slider(f"Dropout Rate (L{i+1})", 0.0, 0.9, 0.0, key=f"d{i}")
                layers_config.append({"neurons": neurons, "activation": activation, "dropout": dropout})
                
            st.markdown("#### Compilation")
            optimizer = st.selectbox("Optimizer", ["adam", "sgd", "rmsprop"])
            if problem_type == "Classification":
                loss = st.selectbox("Loss Function", ["binary_crossentropy", "categorical_crossentropy"])
            else:
                loss = st.selectbox("Loss Function", ["mean_squared_error", "mean_absolute_error"])
                
            epochs = st.number_input("Epochs", 1, 100, 10)
            batch_size = st.number_input("Batch Size", 1, 128, 32)
            
        with col2:
            st.markdown("#### Training Visualization")
            plot_container = st.empty()
            
            if st.button("🔥 Train Neural Network"):
                try:
                    input_dim = X_train.shape[1]
                    model = build_dl_model(input_dim, layers_config, problem_type)
                    
                    with st.spinner("Training Neural Network..."):
                        trained_model, history = compile_and_train(
                            model, optimizer, loss, epochs, batch_size, 
                            X_train, y_train, X_test, y_test, plot_container
                        )
                        
                    st.success("Training Complete!")
                    st.session_state['best_model'] = trained_model
                    
                except Exception as e:
                    st.error(f"DL Training failed: {e}")
