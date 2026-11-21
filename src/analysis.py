"""Expense analysis functions using Pandas and NumPy."""
import numpy as np
import pandas as pd


def category_summary(df):
    result = (df.groupby("category", as_index=False)["amount"]
              .sum().sort_values("amount", ascending=False))
    result["share_percent"] = (
        result["amount"] / result["amount"].sum() * 100
    ).round(2)
    return result


def monthly_summary(df):
    result = (df.groupby("month", as_index=False)["amount"]
              .sum().sort_values("month"))
    result["amount"] = result["amount"].round(2)
    return result


def payment_summary(df):
    return (df.groupby("payment_method", as_index=False)["amount"]
            .sum().sort_values("amount", ascending=False))


def daily_summary(df):
    result = (df.groupby("day", as_index=False)["amount"]
              .sum().sort_values("day"))
    result["day"] = pd.to_datetime(result["day"])
    return result


def build_key_metrics(df):
    total = float(df["amount"].sum())
    category_totals = df.groupby("category")["amount"].sum()
    highest = str(category_totals.idxmax()) if not category_totals.empty else "N/A"
    number_of_days = max(int(df["date"].dt.normalize().nunique()), 1)
    monthly = monthly_summary(df)
    latest_month = monthly.iloc[-1] if not monthly.empty else None

    return {
        "total_expenses": round(total, 2),
        "highest_category": highest,
        "average_daily_spending": round(total / number_of_days, 2),
        "latest_month": str(latest_month["month"]) if latest_month is not None else "N/A",
        "latest_month_spending": round(float(latest_month["amount"]), 2)
            if latest_month is not None else 0.0,
        "transaction_count": int(len(df)),
        "average_transaction": round(float(np.mean(df["amount"])), 2)
    }


def budget_summary(df, monthly_income, monthly_budget):
    monthly = monthly_summary(df)
    if monthly.empty:
        return {"latest_month_status": "No data", "latest_month_remaining": 0.0}

    latest_spend = float(monthly.iloc[-1]["amount"])
    remaining = float(monthly_budget) - latest_spend
    status = "Within budget" if remaining >= 0 else "Over budget"
    return {
        "monthly_income": float(monthly_income),
        "monthly_budget": float(monthly_budget),
        "latest_month_spending": round(latest_spend, 2),
        "latest_month_remaining": round(remaining, 2),
        "latest_month_status": status,
        "income_less_latest_month_spending": round(
            float(monthly_income) - latest_spend, 2
        )
    }
