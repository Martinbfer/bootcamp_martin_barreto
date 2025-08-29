KO Stock Return Prediction Project

Project Overview and Objectives:
This project analyzes and models historical stock returns of Coca-Cola (KO) to estimate the probability of achieving positive 5-year returns.

The workflow follows the full data science lifecycle:
- Data collection and preprocessing
- Feature engineering (lagged returns, rolling volatility, cumulative return)
- Model training (baseline regression & classification)
- Risk evaluation (bootstrap, scenario sensitivity, Monte Carlo)
- Productization with model persistence and API endpoints

Objective: Provide stakeholders with interpretable risk-return insights and a reproducible framework to test assumptions about KO’s performance.

How to Rerun Scripts/Notebooks:

Clone this repository:

git clone <https://github.com/Martinbfer/bootcamp_martin_barreto.git>
cd <C:\Users\marti\bootcamp_martin_barreto\project>


Create and activate the environment:

conda create -n fe-course python=3.11 -y
conda activate fe-course


Install requirements:

pip install -r requirements.txt


Workflow

Data preparation → notebooks/stage06_data-preprocessing.ipynb

Feature engineering & modeling → notebooks/stage10_modeling.ipynb

Evaluation & risk → notebooks/stage11_eval_risk.ipynb

Final reporting → notebooks/stage12_reporting.ipynb

Productization (API + model persistence) → notebooks/stage13_productization.ipynb

Model Persistence


Trained models are saved to:

project/model/model.pkl


You can reload them in Python:

import pickle

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

📊 Assumptions, Risks, and Lifecycle Mapping


Assumptions:

- Past KO returns are representative of future patterns (stationarity assumption).

- Daily returns are i.i.d. within simulation windows (Monte Carlo, bootstrap).

- Missing values are imputed with mean/median strategies.

Risks:

- Structural market changes could invalidate historical assumptions.

- Sensitivity to volatility spikes (extreme events not well captured).

- Model performance metrics show baseline models are weak predictors — risk of overfitting if extended.

Lifecycle Mapping:

Stage 06–10: Data prep & feature engineering

Stage 11: Evaluation & risk analysis (bootstrap, scenarios)

Stage 12: Stakeholder reporting (summary, visuals, sensitivity)

Stage 13: Productization (repo structure, API, persistence)


Instructions for Using the API

The project includes a minimal Flask API in app.py.

Run the API

From the project root:

python app.py


API will be served at http://127.0.0.1:5000/.

Available Endpoints

POST /predict

Send JSON with features:

{
  "volatility_21d": 0.02,
  "cum_return": 0.15
}


Response:

{"prediction": 0.0035}


GET /predict/<volatility>/<cum_return>

Example:

GET /predict/0.02/0.15


Response:

{"prediction": 0.0035}


GET /plot

Returns a simple matplotlib chart (e.g., cumulative returns).


Deliverables

Clean notebooks in /notebooks/

Reusable functions in /src/

Data (processed/raw) in /data/

Pickled model in /model/

Reports and stakeholder summary in /reports/

Final report (Markdown/PDF) in /deliverables/