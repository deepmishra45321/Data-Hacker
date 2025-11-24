import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def build_dl_model(input_dim, layers_config, problem_type):
    """
    Builds a Sequential Keras model based on configuration.
    """
    # Lazy import to avoid heavy startup load
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout

    model = Sequential()
    
    # Input Layer (Implicit in first Dense layer)
    first_layer = True
    
    for layer in layers_config:
        if first_layer:
            model.add(Dense(layer['neurons'], activation=layer['activation'], input_dim=input_dim))
            first_layer = False
        else:
            model.add(Dense(layer['neurons'], activation=layer['activation']))
            
        if layer['dropout'] > 0:
            model.add(Dropout(layer['dropout']))
            
    # Output Layer
    if problem_type == "Classification":
        # Assuming binary classification for simplicity or multi-class if handled.
        # For general purpose, let's assume binary (sigmoid) or multi-class (softmax).
        # We need to know number of classes.
        # For now, let's default to 1 neuron sigmoid for binary, or user needs to specify output.
        # Let's make it simple: 1 neuron sigmoid for binary, N neurons softmax for multi.
        # We'll stick to binary/regression for simplicity or ask user.
        # Let's assume binary for now as per typical simple demos, or check unique values in y.
        model.add(Dense(1, activation='sigmoid')) # Binary Classification
    else:
        model.add(Dense(1, activation='linear')) # Regression
        
    return model

def compile_and_train(model, optimizer, loss_fn, epochs, batch_size, X_train, y_train, X_test, y_test, plot_container):
    """
    Compiles and trains the model with a custom callback for visualization.
    """
    # Lazy import
    from tensorflow.keras.callbacks import Callback

    class StreamlitCallback(Callback):
        def __init__(self, plot_container):
            super().__init__()
            self.plot_container = plot_container
            self.history = {'loss': [], 'accuracy': [], 'val_loss': [], 'val_accuracy': []}
            
        def on_epoch_end(self, epoch, logs=None):
            self.history['loss'].append(logs.get('loss'))
            self.history['accuracy'].append(logs.get('accuracy'))
            self.history['val_loss'].append(logs.get('val_loss'))
            self.history['val_accuracy'].append(logs.get('val_accuracy'))
            
            if epoch % 1 == 0: # Update every epoch
                with self.plot_container:
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
                    
                    ax1.plot(self.history['loss'], label='Train Loss')
                    ax1.plot(self.history['val_loss'], label='Val Loss')
                    ax1.set_title('Loss')
                    ax1.legend()
                    
                    ax2.plot(self.history['accuracy'], label='Train Acc')
                    ax2.plot(self.history['val_accuracy'], label='Val Acc')
                    ax2.set_title('Accuracy')
                    ax2.legend()
                    
                    st.pyplot(fig)

    model.compile(optimizer=optimizer, loss=loss_fn, metrics=['accuracy'])
    
    st_callback = StreamlitCallback(plot_container)
    
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=[st_callback],
        verbose=0
    )
    
    return model, history
