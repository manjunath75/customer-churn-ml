# Customer Churn Prediction

An end-to-end machine learning project that predicts telecom customer churn using Python, scikit-learn, FastAPI, Docker, and GitHub Actions.

The project covers the ML lifecycle from data preparation and model evaluation to serving predictions through a validated REST API and running automated tests in CI.

**Repository:** https://github.com/manjunath75/customer-churn-ml

## Project Overview

Customer churn prediction helps identify customers who may discontinue a service. This project builds a binary classification model using the IBM Telco Customer Churn dataset and serves its predictions through a REST API.

The project prioritizes identifying potential churners while considering the business trade-off between missed churners and false alarms.

## Key Features

- Exploratory data analysis and data cleaning
- Preprocessing with numerical scaling and categorical encoding
- Comparison of Logistic Regression, Decision Tree, Random Forest, and HistGradientBoosting
- Hyperparameter tuning using cross-validation
- Model interpretation using coefficients and permutation importance
- Configurable classification threshold for churn predictions
- FastAPI REST API with Pydantic input validation
- Docker containerization
- Automated API tests with pytest
- GitHub Actions continuous integration

## Tech Stack

**Language:** Python

**Machine Learning:** pandas, NumPy, scikit-learn, joblib

**API:** FastAPI, Pydantic, Uvicorn

**Testing and DevOps:** pytest, HTTPX, Docker, GitHub Actions

## Dataset

The project uses the IBM Telco Customer Churn dataset, containing 7,043 customer records and 21 columns, including customer attributes, subscribed services, billing information, and churn status.

The target variable is `Churn`:

- `Yes`: customer churned
- `No`: customer did not churn

The dataset has an imbalanced target distribution, with approximately 26.5% churners and 73.5% non-churners. Therefore, accuracy alone is not sufficient to evaluate model performance.

## Machine Learning Workflow

1. **Data cleaning:** Converted `TotalCharges` to a numeric type and handled 11 blank values associated with customers having zero tenure.
2. **Exploratory data analysis:** Examined churn patterns across contract types, tenure, internet services, and payment methods.
3. **Preprocessing:** Scaled numerical features and one-hot encoded categorical features.
4. **Data splitting:** Used a stratified train/test split to preserve the target distribution.
5. **Model comparison:** Evaluated Logistic Regression, Decision Tree, Random Forest, and HistGradientBoosting.
6. **Hyperparameter tuning:** Used cross-validation and grid search to select model parameters.
7. **Interpretability:** Examined Logistic Regression coefficients and permutation importance.
8. **Model serving:** Saved the fitted preprocessing and prediction pipeline using joblib and integrated it into FastAPI.

## Model Evaluation

The tuned HistGradientBoosting model achieved the following results on the held-out test set:

| Metric | Result |
|---|---:|
| ROC-AUC | 0.8463 |
| Accuracy at threshold 0.5 | 80.13% |
| Churn recall at threshold 0.5 | Approximately 52% |
| Churn recall at threshold 0.2 | Approximately 86% |
| F1-score at threshold 0.2 | Approximately 0.62 |

The classification threshold affects the balance between precision and recall. A threshold of 0.2 was explored to prioritize detecting potential churners.

For an illustrative cost analysis, a false negative was assigned a cost of ₹5,000 and a false positive a cost of ₹500. These are assumed business costs, not measured costs from a real company.

The threshold decision should ultimately be validated against business requirements and evaluated on data that has not been used for model selection.

## REST API

The FastAPI application exposes the following endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check API health |
| POST | `/predict` | Predict customer churn |

The prediction endpoint accepts customer features, validates the input, and returns the predicted churn probability, classification, and threshold.

Example response:

```json
{
  "churn_probability": 0.82,
  "prediction": "Yes",
  "threshold": 0.2
}
```

The probability shown is illustrative, not the result of a particular customer request.

Interactive API documentation is available at `/docs` when the service is running.

## Project Structure

```text
customer-churn-ml/
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── model/
│   └── churn_pipeline.joblib
├── tests/
│   └── test_api.py
├── data/
├── notebooks/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/manjunath75/customer-churn-ml.git
cd customer-churn-ml
```

### 2. Install dependencies

Python 3.12 is used for the project.

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install project and test dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip install pytest httpx
```

### 3. Run the API

From the repository root:

```bash
uvicorn api.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health

### 4. Run the tests

```bash
python -m pytest -v
```

The API test suite checks the health endpoint, a valid prediction request, and invalid or missing input fields.

### 5. Run with Docker

Build the image:

```bash
docker build -t customer-churn-api .
```

Start the container:

```bash
docker run --rm -p 8000:8000 customer-churn-api
```

Open http://127.0.0.1:8000/docs to test the API.

## Continuous Integration

GitHub Actions automatically runs the test suite when code is pushed or a pull request is opened.

The workflow checks out the repository, sets up Python, installs dependencies, and executes pytest in a GitHub-hosted Ubuntu environment.

## Future Improvements

- Add monitoring for prediction quality and data drift.
- Evaluate probability calibration.
- Add model and dataset versioning.
- Test the API with larger input and load-test scenarios.
- Add a repeatable training pipeline.
- Evaluate the model on newer customer data before deployment.

## Author

**Manjunath A**

Software Engineer | Machine Learning | Generative AI

GitHub: https://github.com/manjunath75

LinkedIn: https://linkedin.com/in/anandmanjunath
