"""Generate deterministic synthetic expense records for project testing."""
from pathlib import Path
import numpy as np
import pandas as pd

CATEGORIES = ["Food", "Transport", "Education", "Shopping",
              "Entertainment", "Bills", "Health"]
PAYMENT_METHODS = ["UPI", "Cash", "Card", "Net Banking"]


def create_sample_expenses(output_path, number_of_records=180, seed=42):
    rng = np.random.default_rng(seed)
    end_date = pd.Timestamp.today().normalize()
    start_date = end_date - pd.DateOffset(months=5)
    days = (end_date - start_date).days

    dates = start_date + pd.to_timedelta(
        rng.integers(0, days + 1, number_of_records), unit="D"
    )
    category_probabilities = [0.27, 0.15, 0.14, 0.16, 0.10, 0.12, 0.06]
    categories = rng.choice(
        CATEGORIES, number_of_records, p=category_probabilities
    )
    amounts = []
    for category in categories:
        ranges = {
            "Food": (50, 450), "Transport": (30, 250),
            "Education": (100, 1200), "Shopping": (100, 1800),
            "Entertainment": (80, 700), "Bills": (150, 1500),
            "Health": (100, 1000)
        }
        low, high = ranges[category]
        amounts.append(round(float(rng.uniform(low, high)), 2))

    data = pd.DataFrame({
        "date": dates.strftime("%Y-%m-%d"),
        "category": categories,
        "amount": amounts,
        "payment_method": rng.choice(PAYMENT_METHODS, number_of_records),
        "description": [f"Sample {category.lower()} expense"
                        for category in categories]
    }).sort_values("date")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_path, index=False)
    return data
