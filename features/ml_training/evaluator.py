"""
ML model evaluation functionality.
"""
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, r2_score, confusion_matrix, mean_squared_error


def evaluate_model(model, X_test, y_test, problem_type):
    """
    Evaluates the model and returns metrics and plots.
    
    Args:
        model: Trained model object
        X_test: Test features
        y_test: Test labels
        problem_type: "Classification" or "Regression"
        
    Returns:
        tuple: (metrics dict, matplotlib figure)
    """
    y_pred = model.predict(X_test)
    metrics = {}
    
    if problem_type == "Classification":
        acc = accuracy_score(y_test, y_pred)
        metrics['Accuracy'] = acc
        cm = confusion_matrix(y_test, y_pred)
        
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_title("Confusion Matrix")
        ax.set_ylabel('Actual')
        ax.set_xlabel('Predicted')
        
        return metrics, fig
        
    elif problem_type == "Regression":
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        metrics['R2 Score'] = r2
        metrics['MSE'] = mse
        
        residuals = y_test - y_pred
        fig, ax = plt.subplots()
        sns.scatterplot(x=y_test, y=residuals, ax=ax)
        ax.axhline(0, color='r', linestyle='--')
        ax.set_title("Residual Plot")
        ax.set_xlabel('Actual Values')
        ax.set_ylabel('Residuals')
        
        return metrics, fig
