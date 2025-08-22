# src/cleaning.py

import pandas as pd

def drop_missing_dates(df, date_col="Date"):
    """
    Remove rows where the date column is missing.
    """
    return df.dropna(subset=[date_col])


def fill_missing_with_ffill(df, cols):
    """
    Forward-fill missing values for given columns.
    Useful for prices or financial series where the last known value is carried forward.
    """
    df[cols] = df[cols].ffill()
    return df


def ensure_numeric(df, cols):
    """
    Convert selected columns to numeric, coercing errors to NaN.
    """
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def add_log_returns(df, price_col="close"):
    """
    Add log returns column based on a price column.
    """
    import numpy as np
    df["log_ret"] = np.log(df[price_col] / df[price_col].shift(1))
    return df
