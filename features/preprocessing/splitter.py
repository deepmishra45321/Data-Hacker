"""
Train-test split functionality.
"""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def split_dataset(df, target_col, test_size, problem_type, random_state=42):
    """
    Splits the dataset into Train and Test sets.
    
    Args:
        df: Input dataframe
        target_col: Name of target column
        test_size: Proportion of data for test set
        problem_type: "Classification" or "Regression"
        random_state: Random seed for reproducibility
        
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    if target_col not in df.columns:
        return None, None, None, None
    
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Handle target encoding for classification if it's categorical
    if problem_type == "Classification" and y.dtype == 'object':
        le = LabelEncoder()
        y = le.fit_transform(y)
        
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    return X_train, X_test, y_train, y_test
