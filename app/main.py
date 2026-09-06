import os

import arviz as az
import numpy as np
import joblib

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TRACE_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "mmm_trace.nc"
)

X_SCALER_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "x_scaler.pkl"
)

Y_SCALER_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "y_scaler.pkl"
)


# Load trained model artifacts
trace = az.from_netcdf(TRACE_PATH)

x_scaler = joblib.load(X_SCALER_PATH)
y_scaler = joblib.load(Y_SCALER_PATH)


# Feature order must exactly match training
FEATURES = [
    "tv_spend_hill",
    "radio_spend_hill",
    "search_spend_hill",
    "facebook_spend_hill",
    "instagram_spend_hill",
    "youtube_spend_hill",
    "display_spend_hill",
    "email_spend_hill",
    "affiliate_spend_hill",
    "price",
    "promotion",
    "holiday",
    "competitor_spend",
]


@app.get("/")
def home():
    return {
        "message": "MMM API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


class PredictionInput(BaseModel):
    tv_spend_hill: float
    radio_spend_hill: float
    search_spend_hill: float
    facebook_spend_hill: float
    instagram_spend_hill: float
    youtube_spend_hill: float
    display_spend_hill: float
    email_spend_hill: float
    affiliate_spend_hill: float

    price: float
    promotion: float
    holiday: float
    competitor_spend: float


@app.post("/predict")
def predict(data: PredictionInput):

    # Create feature vector in the exact training order
    X = np.array([[
        data.tv_spend_hill,
        data.radio_spend_hill,
        data.search_spend_hill,
        data.facebook_spend_hill,
        data.instagram_spend_hill,
        data.youtube_spend_hill,
        data.display_spend_hill,
        data.email_spend_hill,
        data.affiliate_spend_hill,
        data.price,
        data.promotion,
        data.holiday,
        data.competitor_spend,
    ]])

    # Scale input using the scaler fitted during training
    X_scaled = x_scaler.transform(X)

    # Get posterior mean coefficients
    beta_mean = (
        trace.posterior["beta"]
        .mean(
            dim=("chain", "draw")
        )
        .values
    )

    intercept_mean = (
        trace.posterior["intercept"]
        .mean(
            dim=("chain", "draw")
        )
        .values
        .item()
    )

    # Prediction in standardized sales space
    y_scaled_pred = (
        intercept_mean
        + np.dot(
            X_scaled,
            beta_mean
        )
    )

    # Convert prediction back to original sales scale
    y_pred = y_scaler.inverse_transform(
        y_scaled_pred.reshape(-1, 1)
    )[0, 0]

    return {
        "predicted_sales": float(y_pred)
    }