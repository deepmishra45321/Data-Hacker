"""
Categorical encoding functionality.
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def encode_categorical(df, method, columns):
    """
    Encodes categorical columns using Label Encoding or One-Hot Encoding.
    
    Args:
        df: Input dataframe
        method: "Label Encoding" or "One-Hot Encoding"
        columns: List of column names to encode
        
    Returns:
        tuple: (encoded dataframe, dictionary of encoders)
    """
    df_encoded = df.copy()
    encoders = {}
    
    if method == "Label Encoding":
        le = LabelEncoder()
        for col in columns:
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
            encoders[col] = le
    elif method == "One-Hot Encoding":
        df_encoded = pd.get_dummies(df_encoded, columns=columns, drop_first=True)
    
    return df_encoded, encoders
