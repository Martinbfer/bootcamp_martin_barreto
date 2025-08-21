# src/cleaning.py
from __future__ import annotations
import pandas as pd
from typing import Iterable, Literal, Tuple, Dict

def fill_missing_median(
    df: pd.DataFrame,
    columns: Iterable[str] | None = None
) -> tuple[pd.DataFrame, dict[str, float]]:
   
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes("number").columns.tolist()

    medians: Dict[str, float] = {}
    for c in columns:
        med = float(out[c].median())
        medians[c] = med
        out[c] = out[c].fillna(med)
    return out, medians


def drop_missing(
    df: pd.DataFrame,
    threshold: float = 0.5,
    subset: Iterable[str] | None = None
) -> pd.DataFrame:
    """
    Elimina FILAS con más proporción de NaNs que 'threshold'.
    - threshold=0.5 -> si una fila tiene >50% NaN (en subset o en todas), se elimina.
    """
    out = df.copy()
    cols = list(subset) if subset else out.columns.tolist()
    n = len(cols)
    min_non_null = int((1.0 - threshold) * n + 1e-9)
    keep_mask = out[cols].notna().sum(axis=1) >= min_non_null
    return out.loc[keep_mask].copy()


def normalize_data(
    df: pd.DataFrame,
    columns: Iterable[str] | None = None,
    method: Literal["zscore", "minmax"] = "zscore",
    feature_range: Tuple[float, float] = (0.0, 1.0)
) -> tuple[pd.DataFrame, dict[str, tuple[float, float]]]:
   
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes("number").columns.tolist()
    params: Dict[str, Tuple[float, float]] = {}

    a, b = feature_range
    for c in columns:
        s = out[c].astype("float64")
        if method == "zscore":
            mean = float(s.mean())
            std = float(s.std(ddof=0)) or 1.0
            out[c] = (s - mean) / std
            params[c] = (mean, std)
        elif method == "minmax":
            mn, mx = float(s.min()), float(s.max())
            rng = (mx - mn) or 1.0
            out[c] = a + (s - mn) * (b - a) / rng
            params[c] = (mn, mx)
        else:
            raise ValueError("method must be 'zscore' or 'minmax'")
    return out, params
