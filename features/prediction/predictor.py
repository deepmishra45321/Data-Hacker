"""
Prediction functionality.
"""


def make_prediction(model, input_data):
    """
    Makes a prediction using the trained model.
    
    Args:
        model: Trained model object
        input_data: Input dataframe for prediction
        
    Returns:
        Prediction result
    """
    try:
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        raise Exception(f"Prediction error: {e}")


def get_prediction_probability(model, input_data):
    """
    Gets prediction probabilities for classification models.
    
    Args:
        model: Trained model object
        input_data: Input dataframe for prediction
        
    Returns:
        Prediction probabilities if available, None otherwise
    """
    try:
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)
            return proba
        return None
    except Exception as e:
        return None
