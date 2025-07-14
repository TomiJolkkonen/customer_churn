from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_customer

app = FastAPI()

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    Contract: str
    InternetService: str
    SeniorCitizen: int

@app.post("/predict")
def predict(data: CustomerData):
    # Mock input, muunna oikeat featuret mallille sopivaksi
    input_data = [data.tenure, data.MonthlyCharges, data.SeniorCitizen, 1, 0]  # korvaa oikeilla arvoilla
    probability = predict_customer(input_data)
    return {"churn_probability": float(probability)}
