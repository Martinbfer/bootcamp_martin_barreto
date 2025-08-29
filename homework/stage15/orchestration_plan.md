# Stage 15: Orchestration & System Design

## Orchestration Plan

This project follows a structured pipeline for analyzing and modeling Coca-Cola (KO) stock returns.  
The orchestration plan frames the workflow as a Directed Acyclic Graph (DAG) with clearly defined tasks,  
dependencies, inputs, outputs, and monitoring strategies.

---

## 1. Key Tasks and Dependencies

**Pipeline tasks:**
1. **Data Ingestion**  
   - Input: raw CSV/parquet files (`data/raw/ko_data.csv`)  
   - Output: ingested file in `/data/raw/`  
   - Idempotent: Yes (re-download overwrites same path)  

2. **Data Cleaning & Outlier Handling**  
   - Input: raw data  
   - Output: cleaned dataset (`data/processed/ko_cleaned.parquet`)  
   - Idempotent: Yes (always same transformation rules)  

3. **Feature Engineering**  
   - Input: cleaned dataset  
   - Output: features dataset with lag/rolling variables (`data/processed/ko_features.parquet`)  
   - Idempotent: Yes  

4. **Model Training**  
   - Input: features dataset  
   - Output: serialized model (`model/ko_model.pkl`)  
   - Idempotent: No (depends on random seed and retraining window)  

5. **Evaluation & Risk Analysis**  
   - Input: model + features dataset  
   - Output: evaluation metrics (`reports/eval_metrics.json`), risk scenarios (`reports/sensitivity_table.csv`)  
   - Idempotent: Yes, given fixed model  

6. **Reporting**  
   - Input: evaluation outputs  
   - Output: final report (`reports/final_report.md`, `deliverables/stakeholder_summary.pdf`)  
   - Idempotent: Yes  

7. **API/Dashboard Deployment**  
   - Input: trained model  
   - Output: running Flask/Streamlit service (`app.py`, `dashboard.py`)  
   - Idempotent: No (depends on runtime environment)  

**DAG order:**  
