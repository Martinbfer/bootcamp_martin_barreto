1) Load the raw dataset from `data/raw/sample_data.csv`.
2) Baseline check: record shape and missing-value counts per column.
3) Impute numeric NaNs with each column’s **median** and log the medians used.
4) Drop rows that are **>50%** missing (or missing in critical fields, if applicable).
5) Normalize numeric features (**z-score** by default; use **min–max** if a bounded range is required) and log the parameters.
6) Validate: re-check missing counts, compare shapes, and review `describe()` before vs. after.
7) Save the cleaned file to `data/processed/sample_data_cleaned.csv`.
8) Document assumptions & trade-offs (median = robust to outliers; dropping reduces sample size; scaling changes units).
