"""
Data cleaning operations: duplicate removal and missing value handling.
"""
import pandas as pd


def remove_duplicates(df):
    """
    Removes duplicate rows from the dataframe.
    
    Args:
        df: Input dataframe
        
    Returns:
        tuple: (cleaned dataframe, number of rows removed)
    """
    initial_rows = df.shape[0]
    df_clean = df.drop_duplicates()
    final_rows = df_clean.shape[0]
    removed = initial_rows - final_rows
    return df_clean, removed


def handle_missing_values(df):
    """
    Fills missing values (NaN) in the dataframe.
    - Numerical columns: Filled with Mean
    - Categorical columns: Filled with Mode
    
    Args:
        df: Input dataframe
        
    Returns:
        tuple: (cleaned dataframe, dictionary of filled info)
    """
    df_clean = df.copy()
    filled_counts = {}
    
    # Identify columns with missing values
    cols_with_nan = df_clean.columns[df_clean.isna().any()].tolist()
    
    for col in cols_with_nan:
        missing_count = df_clean[col].isna().sum()
        
        if pd.api.types.is_numeric_dtype(df_clean[col]):
            fill_value = df_clean[col].mean()
            df_clean[col] = df_clean[col].fillna(fill_value)
            filled_counts[col] = {
                'type': 'Numerical', 
                'method': 'Mean', 
                'count': missing_count, 
                'value': fill_value
            }
        else:
            # For categorical, use mode (if available)
            if not df_clean[col].mode().empty:
                fill_value = df_clean[col].mode()[0]
                df_clean[col] = df_clean[col].fillna(fill_value)
                filled_counts[col] = {
                    'type': 'Categorical', 
                    'method': 'Mode', 
                    'count': missing_count, 
                    'value': fill_value
                }
            else:
                # Fallback if mode is empty (e.g. all NaNs)
                df_clean[col] = df_clean[col].fillna("Unknown")
                filled_counts[col] = {
                    'type': 'Categorical', 
                    'method': 'Constant', 
                    'count': missing_count, 
                    'value': "Unknown"
                }
                
    return df_clean, filled_counts


def drop_columns(df, columns_to_drop):
    """
    Drops selected columns from the dataframe.
    
    Args:
        df: Input dataframe
        columns_to_drop: List of column names to drop
        
    Returns:
        Dataframe with columns removed
    """
    if columns_to_drop:
        df_clean = df.drop(columns=columns_to_drop)
        return df_clean
    return df


def get_column_types(df):
    """
    Returns lists of numerical and categorical columns.
    
    Args:
        df: Input dataframe
        
    Returns:
        tuple: (list of numeric columns, list of categorical columns)
    """
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    return numeric_cols, categorical_cols
