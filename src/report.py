"""Export analytical tables and a human-readable summary report."""
from pathlib import Path


def save_reports(df, categories, monthly, payments, metrics, budget,
                 output_dir, report_dir):
    output_dir = Path(output_dir)
    report_dir = Path(report_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    categories.to_csv(output_dir / "category_summary.csv", index=False)
    monthly.to_csv(output_dir / "monthly_summary.csv", index=False)
    payments.to_csv(output_dir / "payment_summary.csv", index=False)
    df.to_csv(output_dir / "cleaned_expenses.csv", index=False)

    lines = [
        "PERSONAL EXPENSE TRACKER - SUMMARY REPORT",
        "=" * 48,
        f"Transactions analyzed: {metrics['transaction_count']}",
        f"Total expenses: Rs. {metrics['total_expenses']:,.2f}",
        f"Average transaction: Rs. {metrics['average_transaction']:,.2f}",
        f"Average daily spending: Rs. {metrics['average_daily_spending']:,.2f}",
        f"Highest spending category: {metrics['highest_category']}",
        f"Latest month analyzed: {metrics['latest_month']}",
        f"Latest month spending: Rs. {metrics['latest_month_spending']:,.2f}",
        "",
        "BUDGET SUMMARY",
        f"Monthly income assumption: Rs. {budget.get('monthly_income', 0):,.2f}",
        f"Monthly budget assumption: Rs. {budget.get('monthly_budget', 0):,.2f}",
        f"Latest month budget status: {budget['latest_month_status']}",
        f"Budget remaining (+) / exceeded (-): Rs. {budget['latest_month_remaining']:,.2f}",
        "",
        "CATEGORY BREAKDOWN",
        categories.to_string(index=False),
        "",
        "MONTHLY BREAKDOWN",
        monthly.to_string(index=False),
        "",
        "PAYMENT METHOD BREAKDOWN",
        payments.to_string(index=False),
        "",
        "Note: This report uses manually entered or synthetic data."
    ]
    report_text = "\n".join(lines)
    (report_dir / "expense_summary_report.txt").write_text(
        report_text, encoding="utf-8"
    )
    return report_text
