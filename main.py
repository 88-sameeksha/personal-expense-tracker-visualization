"""Personal Expense Tracker with Data Visualization."""
from pathlib import Path
import pandas as pd

from src.data_generator import create_sample_expenses
from src.data_loader import load_and_clean_expenses
from src.analysis import (
    category_summary, monthly_summary, payment_summary,
    daily_summary, build_key_metrics, budget_summary
)
from src.visualization import create_all_charts
from src.report import save_reports

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
REPORT_DIR = BASE_DIR / "reports"
CHART_DIR = OUTPUT_DIR / "charts"

# Edit these example values to simulate your own monthly finances.
MONTHLY_INCOME = 12000.00
MONTHLY_BUDGET = 9000.00


def main():
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)

    expense_file = DATA_DIR / "expenses.csv"

    # Create a reproducible synthetic dataset if no CSV exists yet.
    if not expense_file.exists():
        print("No expense CSV found. Creating synthetic sample data...")
        create_sample_expenses(expense_file, number_of_records=180)

    print("\nPERSONAL EXPENSE TRACKER")
    print("=" * 45)

    expenses = load_and_clean_expenses(expense_file)
    if expenses.empty:
        print("No valid expense records were found. Check data/expenses.csv.")
        return

    categories = category_summary(expenses)
    monthly = monthly_summary(expenses)
    payments = payment_summary(expenses)
    daily = daily_summary(expenses)
    metrics = build_key_metrics(expenses)
    budget = budget_summary(
        expenses, monthly_income=MONTHLY_INCOME,
        monthly_budget=MONTHLY_BUDGET
    )

    print(f"Valid expense records : {len(expenses)}")
    print(f"Total expenses        : Rs. {metrics['total_expenses']:,.2f}")
    print(f"Average daily spend   : Rs. {metrics['average_daily_spending']:,.2f}")
    print(f"Highest category      : {metrics['highest_category']}")
    print(f"Latest month spending : Rs. {metrics['latest_month_spending']:,.2f}")
    print(f"Monthly budget        : Rs. {MONTHLY_BUDGET:,.2f}")
    print(f"Latest month status   : {budget['latest_month_status']}")
    print(f"Income less all data  : Rs. {MONTHLY_INCOME - metrics['total_expenses']:,.2f}")

    print("\nCATEGORY SUMMARY")
    print(categories.to_string(index=False))
    print("\nMONTHLY SUMMARY")
    print(monthly.to_string(index=False))
    print("\nPAYMENT SUMMARY")
    print(payments.to_string(index=False))

    create_all_charts(
        expenses, categories, monthly, payments, daily, CHART_DIR
    )
    save_reports(
        expenses, categories, monthly, payments, metrics, budget,
        OUTPUT_DIR, REPORT_DIR
    )

    print("\nCompleted successfully.")
    print(f"Charts saved in : {CHART_DIR}")
    print(f"Reports saved in: {OUTPUT_DIR} and {REPORT_DIR}")


if __name__ == "__main__":
    main()
