# Bank Loan Approval Prediction

This repository contains a Streamlit app and a Jupyter notebook for a bank loan approval prediction project using machine learning.

Key files
- [main.py](main.py) — Streamlit application UI and prediction logic. See the model loader [`main.model`](main.py) and the input helper function [`main.user_input_features`](main.py).
- [bankloan.ipynb](bankloan.ipynb) — Notebook with data cleaning, EDA, model training and evaluation.
- [loan_approval_lr_model.joblib](loan_approval_lr_model.joblib) — Saved Logistic Regression model used by the Streamlit app.
- [Bank-Loan-Prediction-Using-machine-Learning/README.md](Bank-Loan-Prediction-Using-machine-Learning/README.md) — additional project copy.

Quick start

1. Create a Python environment (recommended Python 3.8+).
2. Install dependencies:
3.  Run the Streamlit app:
   
Usage
- Open the sidebar form in the running Streamlit app to provide applicant information.
- The app loads the model from [loan_approval_lr_model.joblib](loan_approval_lr_model.joblib) (`main.model`) and shows the prediction.

Notes
- The notebook [bankloan.ipynb](bankloan.ipynb) includes the data preprocessing steps and model training used to produce the saved model.

