"""
ML model training functionality.
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier


def train_model(model_name, problem_type, params, X_train, y_train):
    """
    Trains the selected model with given hyperparameters.
    
    Args:
        model_name: Name of the model to train
        problem_type: "Classification" or "Regression"
        params: Dictionary of hyperparameters
        X_train: Training features
        y_train: Training labels
        
    Returns:
        Trained model object
    """
    model = None
    
    if problem_type == "Classification":
        if model_name == "Logistic Regression":
            model = LogisticRegression(**params)
        elif model_name == "Decision Tree":
            model = DecisionTreeClassifier(**params)
        elif model_name == "Random Forest":
            model = RandomForestClassifier(**params)
        elif model_name == "SVM":
            model = SVC(**params)
        elif model_name == "KNN":
            model = KNeighborsClassifier(**params)
            
    elif problem_type == "Regression":
        if model_name == "Linear Regression":
            model = LinearRegression(**params)
        elif model_name == "Decision Tree":
            model = DecisionTreeRegressor(**params)
        elif model_name == "Random Forest":
            model = RandomForestRegressor(**params)
        elif model_name == "SVR":
            model = SVR(**params)
            
    if model:
        model.fit(X_train, y_train)
        
    return model


def compare_all_models(X_train, X_test, y_train, y_test, problem_type):
    """
    Trains and compares all available models with default parameters.
    
    Args:
        X_train: Training features
        X_test: Test features
        y_train: Training labels
        y_test: Test labels
        problem_type: "Classification" or "Regression"
        
    Returns:
        tuple: (results_df, best_model, best_model_name)
    """
    import numpy as np
    from sklearn.metrics import accuracy_score, r2_score
    
    results = []
    models = {}
    
    if problem_type == "Classification":
        models = {
            "Logistic Regression": LogisticRegression(),
            "Decision Tree": DecisionTreeClassifier(),
            "Random Forest": RandomForestClassifier(),
            "SVM": SVC(),
            "KNN": KNeighborsClassifier()
        }
    elif problem_type == "Regression":
        models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest": RandomForestRegressor(),
            "SVR": SVR()
        }
        
    best_model_name = None
    best_score = -np.inf
    best_model_obj = None
    
    for name, model in models.items():
        try:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            if problem_type == "Classification":
                score = accuracy_score(y_test, y_pred)
                metric_name = "Accuracy"
            else:
                score = r2_score(y_test, y_pred)
                metric_name = "R2 Score"
                
            results.append({"Model": name, metric_name: score})
            
            if score > best_score:
                best_score = score
                best_model_name = name
                best_model_obj = model
                
        except Exception as e:
            results.append({"Model": name, "Error": str(e)})
            
    return pd.DataFrame(results), best_model_obj, best_model_name
