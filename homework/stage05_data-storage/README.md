\# Stage 05 — Data Storage



* Folder Structure

stage05\_data-storage/

├─ notebooks/ 

├─ data/

│ ├─ raw/

│ └─ processed/ 

├─ .env 

└─ README.md



* Formats: Why

CSV (raw): simple, portable, diff-friendly.



Parquet (processed): columnar, compressed, preserves dtypes, faster I/O.



* Environment (.env)

DATA\_DIR\_RAW=data/raw

DATA\_DIR\_PROCESSED=data/processed



Loaded with `python-dotenv`; folders are created with `pathlib` if missing.



* Dataset

\- Source: `yfinance`, Ticker: `MSFT`, Start: `2024-01-01`, `auto\_adjust=True`.

\- Standardized columns: `date`, `ticker`, `price`.



* Utilities (summary)

write\_df(df, path): writes by suffix (.csv or .parquet), creates parent dirs, friendly Parquet error.



read\_df(path): reads by suffix; parses date on CSV if present.



* Validation

Shapes match (original vs reloaded).



date is datetime64.



price is numeric and has no NAs.





