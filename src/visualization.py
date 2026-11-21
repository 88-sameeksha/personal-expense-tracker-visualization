"""Create and save expense visualization charts."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")  # Allows charts to be saved in terminals/headless systems.
import matplotlib.pyplot as plt
import seaborn as sns


def create_all_charts(df, categories, monthly, payments, daily, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    # 1. Category-wise bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(data=categories, x="amount", y="category", color="steelblue")
    plt.title("Expense by Category")
    plt.xlabel("Amount (INR)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(output_dir / "category_wise_expenses.png", dpi=150)
    plt.close()

    # 2. Monthly spending line chart
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly, x="month", y="amount", marker="o", color="darkorange")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount (INR)")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.savefig(output_dir / "monthly_spending_trend.png", dpi=150)
    plt.close()

    # 3. Payment method pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        payments["amount"], labels=payments["payment_method"],
        autopct="%1.1f%%", startangle=90
    )
    plt.title("Spending by Payment Method")
    plt.tight_layout()
    plt.savefig(output_dir / "payment_method_distribution.png", dpi=150)
    plt.close()

    # 4. Daily spending trend chart
    plt.figure(figsize=(11, 5))
    sns.lineplot(data=daily, x="day", y="amount", color="seagreen")
    plt.title("Daily Spending Trend")
    plt.xlabel("Date")
    plt.ylabel("Amount (INR)")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.savefig(output_dir / "daily_spending_trend.png", dpi=150)
    plt.close()
