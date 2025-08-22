def clean_column_names(columns):
    """
    Clean column names by:
    - Stripping whitespace
    - Lowercasing
    - Replacing spaces with underscores
    
    Args:
        columns (list or Index): List of column names
    
    Returns:
        list: Cleaned column names
    """
    return [col.strip().lower().replace(" ", "_") for col in columns]

import pandas as pd

def parse_dates(df, column):
    """
    Convert a column in a DataFrame to datetime format.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        column (str): Column name to convert
    
    Returns:
        pd.DataFrame: Updated DataFrame with parsed datetime column
    """
    df[column] = pd.to_datetime(df[column], errors="coerce")
    return df
