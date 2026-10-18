
# Customer Churn Prediction

An end-to-end machine learning project that predicts
telecom customer churn using a trained classification
pipeline, FastAPI, Docker, and GitHub Actions.

## Features

- Data cleaning and exploratory data analysis
- Logistic Regression, Decision Tree, Random Forest,
  and HistGradientBoosting model comparison
- Hyperparameter tuning using cross-validation
- Churn prediction with a configurable probability threshold
- REST API built with FastAPI and Pydantic validation
- Docker containerization
- Automated API tests using pytest
- Continuous integration using GitHub Actions

## Tech Stack

Python, pandas, NumPy, scikit-learn, FastAPI,
Pydantic, joblib, pytest, Docker, GitHub Actions

## Project Structure

- `api/` - FastAPI application and request schemas
- `model/` - Saved trained ML pipeline
- `tests/` - Automated API tests
- `notebooks/` - Data analysis and model development
- `data/` - Dataset files
- `Dockerfile` - Container configuration
- `requirements.txt` - Python dependencies
- `.github/workflows/` - CI workflow

## Run Locally

Create and activate a virtual environment, then install
the dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip install pytest httpx
```

Run the API from the project root:

```bash
uvicorn api.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health

## Run Tests

```bash
python -m pytest -v
```

## Run with Docker

Build the image:

```bash
docker build -t customer-churn-api .
```

Run the container:

```bash
docker run --rm -p 8000:8000 customer-churn-api
```

Open http://127.0.0.1:8000/docs

## Model Evaluation

The tuned HistGradientBoosting model achieved
approximately 0.846 ROC-AUC on the held-out test set.

At a probability threshold of 0.2, churn recall was
approximately 0.86 on the test set.

The threshold was selected to prioritize identifying
potentially churning customers under an assumed
false-negative cost higher than the false-positive cost.

These results are dataset-specific and do not guarantee
the same performance in production.

## Continuous Integration

GitHub Actions installs the dependencies and runs the
automated tests on pushes and pull requests.

## Future Improvements

- Add model monitoring and data drift detection
- Evaluate probability calibration
- Add model and data versioning
- Deploy the API to a cloud platform
