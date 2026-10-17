from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

VALID_CUSTOMER = {
    "tenure": 12,
    "MonthlyCharges": 70.5,
    "TotalCharges": 850.0,
    "SeniorCitizen": 0,
    "gender": "Female",
    "Partner": "No",
    "Dependents": "No",
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
}


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_predict_valid_customer():
    response = client.post("/predict", json=VALID_CUSTOMER)

    assert response.status_code == 200

    result = response.json()
    assert 0 <= result["churn_probability"] <= 1
    assert result["prediction"] in ["Yes", "No"]
    assert result["threshold"] == 0.2


def test_predict_invalid_contract():
    customer = VALID_CUSTOMER.copy()
    customer["Contract"] = "monthly"

    response = client.post("/predict", json=customer)

    assert response.status_code == 422


def test_predict_missing_tenure():
    customer = VALID_CUSTOMER.copy()
    customer.pop("tenure")

    response = client.post("/predict", json=customer)

    assert response.status_code == 422