# Credit Risk Analysis

Credit risk EDA + baseline models to predict loan default risk using Python.

## What this project does
- Cleans and explores a public credit dataset
- Creates clear, reproducible visualizations (exported to `reports/figures/`)
- Builds baseline models as a starting point for default-risk prediction

## Repo structure
- `Notebooks/` – step-by-step notebooks (loading/cleaning + analysis)
- `data/` – public dataset used in this project
- `reports/figures/` – exported charts (PNG)
- `src/` – small helper modules

## Key outputs
- Correlation heatmap (`correlation_matrix.png`)
- Missing values overview (`missing_values_percent.png`)
- Interest rate vs. loan status (`loan_int_rate_by_loan_status.png`)

## Tech stack
Python, pandas, matplotlib, scikit-learn

## Next improvements
- Proper train/validation split + cross-validation
- Handle class imbalance (e.g., class weights / resampling)
- Model comparison + calibration (ROC-AUC, PR-AUC)
- Feature importance + error analysis

## How to run
pip install -r requirements.txt
