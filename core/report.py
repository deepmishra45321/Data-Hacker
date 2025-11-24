"""
Report utility module.
"""
import datetime


def generate_report(data_snapshot, cleaned_data, best_model):
    """
    Generates a text report summarizing the session.
    
    Args:
        data_snapshot: Dictionary with data snapshot info
        cleaned_data: Dictionary with cleaned/processed data info
        best_model: Trained model object
        
    Returns:
        str: Formatted report text
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Safely extract X_train and X_test
    X_train = cleaned_data.get('X_train') if cleaned_data else None
    X_test = cleaned_data.get('X_test') if cleaned_data else None
    
    # Get training and test set sizes
    train_size = X_train.shape[0] if X_train is not None else 'N/A'
    test_size = X_test.shape[0] if X_test is not None else 'N/A'
    
    report = f"""
    ========================================
    DATA HUNTING - AUTOMATED REPORT
    ========================================
    Generated on: {timestamp}
    
    1. DATA SNAPSHOT
    ----------------
    Rows: {data_snapshot.get('rows', 'N/A')}
    Columns: {data_snapshot.get('cols', 'N/A')}
    Duplicates Removed: {data_snapshot.get('duplicates', 'N/A')}
    
    2. PREPROCESSING
    ----------------
    Target Variable: {cleaned_data.get('target_col', 'N/A') if cleaned_data else 'NA'}
    Problem Type: {cleaned_data.get('problem_type', 'N/A') if cleaned_data else 'N/A'}
    Training Set Size: {train_size}
    Test Set Size: {test_size}
    
    3. MODEL PERFORMANCE
    --------------------
    Best Model: {best_model.__class__.__name__ if best_model else 'None'}
    
    ========================================
    END OF REPORT
    ========================================
    """
    return report
