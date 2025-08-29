# Lifecycle Framework Guide — KO Stock Return Prediction Project

## Problem Framing
- **Goal:** Estimate probability that Coca-Cola (KO) will deliver positive returns over a 5-year horizon.  
- **Stakeholders:** Investors, analysts, risk managers.  
- **Decision Context:** Support long-term investment decisions with risk-aware metrics.

## Data
- **Source:** Historical KO stock price and return data (CSV/parquet).  
- **Raw data location:** `/data/raw/`  
- **Processed data:** `/data/processed/ko_cleaned.parquet`  
- **Assumptions:** Historical daily returns approximate future behavior.  
- **Risks:** Schema drift, missing values, delayed labels.

## Cleaning & Preprocessing
- Outlier detection (IQR, z-score).  
- Null handling (forward-fill, imputation).  
- Outputs stored as parquet checkpoints in `/data/processed/`.  
- Documented in `README.md` and `outliers.py`.

## Feature Engineering
- Lag features (`lag1`, `lag2`).  
- Rolling volatility (21-day).  
- Cumulative return.  
- Outputs in `/data/processed/ko_features.parquet`.  
- Reusable code in `/src/features.py`.

## Modeling
- Baseline linear regression (Stage 10a).  
- Classification model predicting up/down returns (Stage 10b).  
- Saved model: `/model/ko_model.pkl`.  
- Evaluation metrics: RMSE, MAE, accuracy.

## Evaluation & Risk
- Bootstrap confidence intervals for 5-year probability.  
- Monte Carlo scenarios (Normal vs. resampling).  
- Subgroup analysis by era (2000–05, 2006–10, etc.).  
- Outputs in `/reports/eval_metrics.json`, `/reports/sensitivity_table.csv`.

## Reporting
- Stakeholder summary: `/reports/final_report.md`, `/deliverables/stakeholder_summary.pdf`.  
- 2–3 key charts: cumulative return, scenario probabilities, subgroup diagnostics.  
- Executive summary written in plain language for decision-makers.

## Productization
- Flask API (`app.py`) with `/predict` and `/plot`.  
- Model persistence (`/model/ko_model.pkl`).  
- Optional Streamlit dashboard (`dashboard.py`).  
- `requirements.txt` for reproducibility.

## Deployment & Monitoring
- Risks: schema drift, concept drift, outages.  
- Monitoring layers: Data (nulls, schema), Model (AUC, PSI), System (latency, uptime), Business (hit rate).  
- Runbook and ownership defined in `reflection.md`.

## Orchestration
- Pipeline DAG: Ingest → Clean → Feature Engineering → Train → Evaluate → Report → Deploy.  
- Checkpoints at every stage (data parquet, model pickle, metrics JSON).  
- Automation: preprocessing + modeling scripts; Manual: report interpretation.  
- Logged in `orchestration_plan.md`.

## Lifecycle Integration
- **Stage 08–09:** Data exploration & features.  
- **Stage 10–11:** Modeling + evaluation.  
- **Stage 12:** Reporting for stakeholders.  
- **Stage 13–15:** Productization, orchestration, deployment.  
- **Stage 16:** Final polish and submission.

---

## Final Repo Checklist
- ✅ `/data/` — raw and processed datasets.  
- ✅ `/src/` — reusable functions (`features.py`, `outliers.py`, etc.).  
- ✅ `/notebooks/` — staged, cleaned notebooks.  
- ✅ `/model/` — persisted pickle model.  
- ✅ `/reports/` — metrics, sensitivity tables, final report.  
- ✅ `/deliverables/` — stakeholder-friendly summary.  
- ✅ `README.md` — overview, lifecycle mapping, API instructions.  
- ✅ `requirements.txt` — dependencies.  
