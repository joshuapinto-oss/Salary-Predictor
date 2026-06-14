# Data Science Salary Predictor

A machine learning web app that predicts data science salaries (in USD) based on experience level, employment type, job title, company size and remote work ratio.

## Overview

This project uses a Linear Regression model trained on the [Data Science Job Salaries dataset](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries) from Kaggle. It demonstrates an end-to-end machine learning workflow: data preprocessing, model training, evaluation, and deployment as an interactive web app.

## Tech Stack

- **Python**
- **Pandas** – data loading and manipulation
- **Scikit-learn** – ColumnTransformer, OneHotEncoder, StandardScaler, Pipeline, Linear Regression
- **Streamlit** – web app interface
- **Joblib** – model serialization

## How It Works

1. **Preprocessing** – Categorical features (experience level, employment type, job title, company size) are encoded using `OneHotEncoder`. The numerical feature (remote work ratio) is scaled using `StandardScaler`. Both steps are combined using `ColumnTransformer`.
2. **Pipeline** – Preprocessing and the Linear Regression model are bundled into a single `Pipeline`, so the entire workflow (transform + predict) runs in one step.
3. **Training** – The pipeline is trained on an 80/20 train-test split and evaluated using MAE and R² score.
4. **Deployment** – The trained pipeline is saved with `joblib` and loaded into a Streamlit app, where users can input their details via dropdowns and get an instant salary prediction.

## Live Demo

https://salary-predictor-nyvs8c2n7wcqt5fb3gsyge.streamlit.app/

## Features Used

| Feature | Description |
| 'experience_level' | EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| 'employment_type' | FT (Full-time), PT (Part-time), CT (Contract), FL (Freelance) |
| 'job_title' | e.g. Data Scientist, ML Engineer, Data Analyst |
| 'company_size' | S (Small), M (Medium), L (Large) |
| 'remote_ratio' | 0, 50, or 100 (% remote work) |

## Running Locally

```bash
# Clone the repo
git clone <repo-url>
cd salary-predictor

# Install dependencies
pip install -r requirements.txt

# Run the model training notebook (generates model.pkl)
# Open and run main.ipynb in Jupyter / VS Code

# Run the app
streamlit run app.py

## Project Files

- main.ipynb – notebook that loads data, builds the preprocessing + model pipeline, trains, evaluates and saves 'model.pkl'
- app.py – Streamlit app that loads 'model.pkl' and serves predictions
- model.pkl – saved trained pipeline
- ds_salaries.csv – dataset used for training
- requirements.txt – Python dependencies

## Future Improvements

- Add more features ('company_location', 'employee_residence', 'work_year') to improve prediction accuracy
- Try other models (Random Forest, Gradient Boosting) for comparison
- Add input validation and confidence intervals to predictions

## Author

Joshua Pinto 