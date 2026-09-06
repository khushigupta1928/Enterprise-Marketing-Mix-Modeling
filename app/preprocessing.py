import pandas as pd

from .transformations import adstock_transform, hill_saturation


def prepare_data(file_path):
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    decay_rates = {
        "tv_spend": 0.80,
        "radio_spend": 0.50,
        "search_spend": 0.30,
        "facebook_spend": 0.60,
        "instagram_spend": 0.55,
        "youtube_spend": 0.70,
        "display_spend": 0.40,
        "email_spend": 0.20,
        "affiliate_spend": 0.35,
    }

    for channel, decay in decay_rates.items():
        df[channel + "_adstock"] = adstock_transform(
            df[channel],
            decay
        )

    hill_params = {
        "tv_spend_adstock": (1.5, 1500000),
        "radio_spend_adstock": (1.3, 300000),
        "search_spend_adstock": (1.8, 700000),
        "facebook_spend_adstock": (1.6, 500000),
        "instagram_spend_adstock": (1.5, 450000),
        "youtube_spend_adstock": (1.7, 800000),
        "display_spend_adstock": (1.2, 250000),
        "email_spend_adstock": (1.1, 100000),
        "affiliate_spend_adstock": (1.2, 180000),
    }

    for channel, (alpha, gamma) in hill_params.items():
        new_col = channel.replace("_adstock", "_hill")
        df[new_col] = hill_saturation(
            df[channel],
            alpha,
            gamma
        )

    return df