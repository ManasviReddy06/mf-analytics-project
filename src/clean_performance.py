import os
import pandas as pd

RAW = "data/raw/07_scheme_performance.csv"
OUT = "data/processed/07_scheme_performance.csv"

os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("Cleaning Scheme Performance")
print("=" * 60)

df = pd.read_csv(RAW)

print("Rows before cleaning :", len(df))

# -----------------------------
# Convert return columns
# -----------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# Expense Ratio Validation
# -----------------------------

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:", len(invalid_expense))

if len(invalid_expense) > 0:
    print(invalid_expense[
        ["scheme_name", "expense_ratio_pct"]
    ])

# -----------------------------
# Missing Values
# -----------------------------

print("\nMissing Values")

print(df.isnull().sum())

# -----------------------------
# Remove Duplicates
# -----------------------------

before = len(df)

df = df.drop_duplicates()

after = len(df)

print("\nDuplicates Removed :", before-after)

# -----------------------------
# Save
# -----------------------------

df.to_csv(
    OUT,
    index=False
)

print("\nRows after cleaning :", len(df))

print("\nSaved :", OUT)