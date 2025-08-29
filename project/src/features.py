# src/features.py
import pandas as pd

def make_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "Date" in df.columns:
        df = df.sort_values("Date").reset_index(drop=True)
    if "daily_ret" not in df.columns and "close" in df.columns:
        df["daily_ret"] = df["close"].pct_change()
    df["lag1"] = df["daily_ret"].shift(1)
    df["volatility_21d"] = df["daily_ret"].rolling(21, min_periods=21).std()
    return df
