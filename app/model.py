import pymc as pm


def build_mmm_model(X_scaled, y_scaled):
    with pm.Model() as model:
        intercept = pm.Normal("intercept", mu=0, sigma=1)

        beta = pm.Normal(
            "beta",
            mu=0,
            sigma=1,
            shape=X_scaled.shape[1]
        )

        sigma = pm.HalfNormal("sigma", sigma=1)

        mu = intercept + pm.math.dot(X_scaled, beta)

        pm.Normal(
            "sales",
            mu=mu,
            sigma=sigma,
            observed=y_scaled
        )

    return model