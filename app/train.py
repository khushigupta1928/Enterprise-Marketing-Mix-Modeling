import os

import arviz as az
import joblib
import pandas as pd
import pymc as pm
from sklearn.preprocessing import StandardScaler

from .model import build_mmm_model
from .preprocessing import prepare_data


DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "enterprise_mmm_final.csv"
)


def train_model():
    # 1. Prepare data
    df = prepare_data(DATA_PATH)

    # 2. Select MMM features
    features = [
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

    X = df[features]
    y = df["sales"]

    # 3. Scale X and y
    x_scaler = StandardScaler()
    y_scaler = StandardScaler()

    X_scaled = x_scaler.fit_transform(X)

    y_scaled = y_scaler.fit_transform(
        y.to_numpy().reshape(-1, 1)
    ).flatten()

    # 4. Build Bayesian MMM
    model = build_mmm_model(
        X_scaled,
        y_scaled
    )

    # 5. Train using MCMC
    with model:
        trace = pm.sample(
            draws=500,
            tune=500,
            chains=2,
            target_accept=0.95,
            random_seed=42
        )

    # 6. Save scalers and model results
    artifacts_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "artifacts"
    )

    os.makedirs(
        artifacts_path,
        exist_ok=True
    )

    joblib.dump(
        x_scaler,
        os.path.join(
            artifacts_path,
            "x_scaler.pkl"
        )
    )

    joblib.dump(
        y_scaler,
        os.path.join(
            artifacts_path,
            "y_scaler.pkl"
        )
    )

    trace.to_netcdf(
        os.path.join(
            artifacts_path,
            "mmm_trace.nc"
        )
    )

    print("MMM model training completed.")

    return trace


if __name__ == "__main__":
    train_model()