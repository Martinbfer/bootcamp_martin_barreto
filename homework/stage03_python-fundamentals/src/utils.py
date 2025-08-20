from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np

def load_data(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    return pd.read_csv(path)

def get_summary_stats(df: pd.DataFrame, by: str | None = None) -> pd.DataFrame:
    if by is None:
        return df.describe().T
    if by not in df.columns:
        raise KeyError(f"La columna '{by}' no está en el DataFrame.")
    numeric_cols = df.select_dtypes(include="number").columns
    agg_map = {col: ["count", "mean", "std", "min", "median", "max"] for col in numeric_cols}
    grouped = df.groupby(by, dropna=False).agg(agg_map)
    grouped.columns = ["_".join(filter(None, map(str, c))).strip("_") for c in grouped.columns.values]
    return grouped.reset_index()

def save_table(df: pd.DataFrame, out_csv: str | Path | None = None, out_json: str | Path | None = None) -> None:
    if out_csv:
        out_csv = Path(out_csv)
        out_csv.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(out_csv, index=False)
    if out_json:
        out_json = Path(out_json)
        out_json.parent.mkdir(parents=True, exist_ok=True)
        df.to_json(out_json, orient="records", lines=False, indent=2)

def vectorized_vs_loop(n: int = 1_000_000) -> dict[str, float]:
    import time
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)
    t0 = time.perf_counter()
    b = [x**2 + 2*x + 1 for x in a]
    t_loop = time.perf_counter() - t0
    t0 = time.perf_counter()
    c = a**2 + 2*a + 1
    t_vec = time.perf_counter() - t0
    assert np.allclose(np.array(b, dtype=np.float64), c)
    return {"t_loop_s": t_loop, "t_vectorized_s": t_vec, "speedup_x": t_loop / t_vec if t_vec > 0 else float("inf")}
