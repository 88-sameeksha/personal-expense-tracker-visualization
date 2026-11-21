"""Load, validate, and clean expense records."""
import pandas as pd

REQUIRED_COLUMNS = [
    "date", "category", "amount", "payment_method", "description"
]


def load_and_clean_expenses(csv_path):
    df = pd.read_csv(csv_path)
    missing_columns = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_columns:
        raise ValueError(f"CSV is missing required columns: {missing_columns}")

    df = df[REQUIRED_COLUMNS].copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    for column in ["category", "payment_method", "description"]:
        df[column] = df[column].fillna("").astype(str).str.strip()

    # Reject rows with invalid dates, non-positive amounts, or blank labels.
    df = df.dropna(subset=["date", "amount"])
    df = df[df["amount"] > 0]
    df = df[
        (df["category"] != "") &
        (df["payment_method"] != "")
    ].copy()

    df["category"] = df["category"].str.title()
    df["payment_method"] = df["payment_method"].str.title()
    df["description"] = df["description"].replace("", "No description")
    df["month"] = df["date"].dt.to_period("M").astype(str)
    df["day"] = df["date"].dt.date
    return df.sort_values("date").reset_index(drop=True)
