Project Title:
Will Coca-Cola (KO) Stocks have positive returns in 5 years?
Stage: Problem Framing & Scoping (Stage 01)

Problem Statement:
In long-term investments it is important to assess if the stock's prices will give a positive return. This project will analyze if an investor that buys Coca-Cola (KO) today will receive positive return over a fixed 5-year period under a buy & hold strategy. 
I use public historical data (Yahoo Finance) to evaluate 5-year holding periods across KO’s history and to provide a predictive answer based on an estimate of the probability of a positive outcome.

Stakeholder & User:
Stakeholder: Individual investor or portfolio manager.
User: Investor, portfolio manager.

Decision window: 
Annual review (long-term).

Useful Answer & Decision:
Type: Predictive

Metric: 
Probability estimate through historical records (share of 5-year windows with positive return).

Assumptions & Constraints:
Data: Yahoo Finance daily adjusted close 
Liquidity & capacity
Stationarity: historical data does not guarantee results.

Known Unknowns / Risks:
Regime change 

Lifecycle Mapping
Goal → Stage → Deliverable
Goal 1 → Problem Framing & Scoping (Stage 01) → Problem Statement & Memo
Goal 2 → Tooling Setup → Github repo with files
Goal 3 → Data Acquisition/Ingestion → Github with data files
Goal 4 → Data Storage 
Goal 5 → Data Preprocessing
Goal 6 → Outlier Analysis
Goal 7 → Exploratory Data Analysis
Goal 8 → Feature Engineering
Goal 9 → Modeling
Goal 10 → Evaluation & Risk Comunnication
Goal 11 → Results Reporting, Delivery Design & Stakeholder Communication


- Data Storage:

The project's folder structure for storing data:

data/raw/ contains the raw datasets exactly as downloaded from the source (Coca-Cola stock prices in CSV, financial statements in JSON).

data/processed/ contains datasets prepared for analysis (daily returns saved in Parquet format).

Raw data is always preserved in CSV/JSON, while processed data is stored in Parquet.

All data paths are managed in a reproducible way. By default, the code reads and writes to the data/ folder at the project root. 

- Data preprocessing

Preprocessing was applied to the Coca-Cola dataset to prepare it for modeling.  
Steps included:

- Dropping rows with missing dates.  
- Converting price and return columns to numeric types.  
- Forward-filling missing values to maintain continuity in time series.  
- Adding log returns for use in financial models.  

The preprocessing functions are stored in `src/cleaning.py` for reusability.  
A demonstration of the pipeline is provided in `notebooks/data_preprocessing.ipynb`.  
The cleaned dataset is saved in `data/processed/ko_cleaned.parquet`.  

Assumptions:
Missing Dates: Rows with missing dates were dropped to maintain consistent time series continuity. This ensures calculations like returns are accurate.

Numeric Conversion: Columns close and daily_ret were explicitly converted to numeric to avoid issues with string or object types.

Forward Fill: Any missing values in close or daily_ret were filled using forward fill (propagating the last valid value). This prevents breaks in the time series caused by isolated gaps.

Log Returns: A new column log_ret was added to capture log returns.

- Outlier Handling (Stage 7)

I applied the IQR method (k=1.5) on daily_ret to flag outliers.

Cutoffs: –0.0232 (Q1–1.5×IQR), +0.0238 (Q3+1.5×IQR)


Impact: mean shifted slightly closer to the median (0.00034 → 0.00047), and std dropped from 0.0129 to 0.0086, showing that extreme returns were driving most of the variance.

Assumptions ans risk:

Outliers outside 1.5×IQR represent anomalies rather than the “typical” return process.

Data quality is reliable, and extreme points are not caused by reporting errors.

In financial data, such “outliers” often correspond to real market events (crashes/spikes). Removing them stabilizes the dataset but the risk is underestimating true risk. 

- Stage09: Feature engineering

Feature 1: Rolling Volatility (21 days)

This feature measures the short-term risk of the asset, calculated as the standard deviation of daily returns over the past 21 trading days (about one month). By using rolling volatility, the model can capture time-varying risk levels instead of assuming that volatility is constant. This is important in financial markets because periods of high volatility often coincide with crises, uncertainty, or structural changes in returns.

Feature 2: Cumulative Return

This feature represents the total growth of an investment over time if an investor had put $1 at the start date. It captures long-term performance trends and helps contextualize whether short-term movements (daily or monthly returns) are happening in a generally positive or negative growth environment. This can be especially useful for detecting regime shifts (e.g., moving from a bull to a bear market).