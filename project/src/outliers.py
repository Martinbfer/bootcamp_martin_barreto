# src/outliers.py
from __future__ import annotations
import pandas as pd
from typing import Tuple, Optional

def detect_outliers_iqr(
    series: pd.Series,
    k: float = 1.5,
    return_bounds: bool = False,
) -> pd.Series | Tuple[pd.Series, Tuple[float, float]]:
   
    s = pd.to_numeric(series, errors="coerce")
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1

    if pd.isna(iqr) or iqr == 0:
        mask = pd.Series(False, index=series.index)
        return (mask, (float(q1), float(q3))) if return_bounds else mask

    lower = q1 - k * iqr
    upper = q3 + k * iqr
    mask = (s < lower) | (s > upper)
    return (mask, (float(lower), float(upper))) if return_bounds else mask
