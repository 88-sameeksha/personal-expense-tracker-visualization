# Interview Preparation

## 1. Explain your project.
I developed a Python-based Personal Expense Tracker that reads expense records from CSV, cleans and validates the data, analyzes spending by category, month, day, and payment method, and generates visualizations and reports. I used Pandas and NumPy for analysis and Matplotlib and Seaborn for charts. The project uses sample or manually entered data and does not connect to banking systems.

## 2. Why did you use Pandas?
Pandas provides DataFrames and convenient functions for reading CSV files, cleaning missing values, grouping transactions, and calculating aggregations.

## 3. What is data cleaning?
Data cleaning is the process of detecting and handling invalid or inconsistent records. Here I convert dates and amounts to appropriate types and exclude rows with invalid dates, non-positive amounts, or missing category/payment labels.

## 4. What is groupby()?
`groupby()` splits data into groups based on one or more columns and lets us calculate summaries such as total spending per category.

## 5. Why use NumPy?
NumPy supports efficient numerical operations. In this project it is used to generate reproducible synthetic data and calculate numerical summaries.

## 6. What is the difference between Matplotlib and Seaborn?
Matplotlib is a general-purpose plotting library. Seaborn is built on Matplotlib and provides a higher-level interface for statistical visualizations and attractive defaults.

## 7. How do you calculate average daily spending?
The project divides total expenses by the number of distinct dates on which valid expenses were recorded. This is average spending per active expense day, not necessarily per calendar day.

## 8. How do you identify overspending?
The project compares the latest month's total expense with the configured monthly budget. If expenses exceed the budget, the status is marked Over budget.

## 9. Why did you use CSV instead of a database?
CSV is lightweight, easy to inspect, and suitable for a student project without external services. A future version could use SQLite for structured queries and more robust storage.

## 10. What would you improve next?
I would add a Streamlit dashboard, interactive date/category filters, SQLite storage, automated tests, and a form for adding expenses.

## HR / Non-technical explanation

I wanted to build a practical Python project that solves a familiar problem: understanding spending habits. I created a tool that organizes expense records and turns them into clear summaries and charts. Through this project, I practiced problem-solving, structured coding, data analysis, visualization, documentation, and GitHub version control.
