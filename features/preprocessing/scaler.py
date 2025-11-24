"""
Feature scaling functionality.
"""
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def scale_features(df, method, target_col=None):
    """
    Scales numerical features using StandardScaler or MinMaxScaler.
    Excludes the target column from scaling.
    
    Args:
        df: Input dataframe
        method: "StandardScaler", "MinMaxScaler", or "None"
        target_col: Name of target column to exclude from scaling
        
    Returns:
        tuple: (scaled dataframe, scaler object)
    """
    scaler = None
    df_scaled = df.copy()
    
    # Identify numerical columns to scale (exclude target)
    numeric_cols = df_scaled.select_dtypes(include=['number']).columns.tolist()
    if target_col in numeric_cols:
        numeric_cols.remove(target_col)
        
    if not numeric_cols:
        return df_scaled, None

    if method == "StandardScaler":
        scaler = StandardScaler()
    elif method == "MinMaxScaler":
        scaler = MinMaxScaler()
    
    if scaler:
        df_scaled[numeric_cols] = scaler.fit_transform(df_scaled[numeric_cols])
        
    return df_scaled, scaler
