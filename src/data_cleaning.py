import os
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

print("=" * 70)
print("DAY 2 - DATA CLEANING")
print("=" * 70)

# ======================================================
# 1. CLEAN NAV HISTORY
# ======================================================

print("\nCleaning 02_nav_history.csv...")

nav = pd.read_csv(f"{RAW_DIR}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
nav = nav.dropna(subset=["date"])

nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED_DIR}/02_nav_history.csv",
    index=False
)

print("✓ NAV history cleaned")

# ======================================================
# 2. CLEAN INVESTOR TRANSACTIONS
# ======================================================

print("\nCleaning 08_investor_transactions.csv...")

txn = pd.read_csv(f"{RAW_DIR}/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn = txn.dropna(subset=["transaction_date"])

txn["transaction_type"] = (
    txn["transaction_type"]
        .astype(str)
        .str.strip()
        .str.upper()
)

txn["transaction_type"] = txn["transaction_type"].replace({
    "SYSTEMATIC INVESTMENT PLAN": "SIP",
    "SYSTEMATIC INVESTMENT": "SIP",
    "LUMP SUM": "LUMPSUM",
    "LUMP-SUM": "LUMPSUM",
    "ONE TIME": "LUMPSUM"
})

txn["amount_inr"] = pd.to_numeric(
    txn["amount_inr"],
    errors="coerce"
)

txn = txn[txn["amount_inr"] > 0]

txn["kyc_status"] = (
    txn["kyc_status"]
        .astype(str)
        .str.upper()
        .str.strip()
)

valid_status = [
    "VERIFIED",
    "PENDING",
    "REJECTED"
]

txn.loc[
    ~txn["kyc_status"].isin(valid_status),
    "kyc_status"
] = "UNKNOWN"

txn = txn.drop_duplicates()

txn.to_csv(
    f"{PROCESSED_DIR}/08_investor_transactions.csv",
    index=False
)

print("✓ Investor transactions cleaned")

# ======================================================
# 3. CLEAN SCHEME PERFORMANCE
# ======================================================

print("\nCleaning 07_scheme_performance.csv...")

perf = pd.read_csv(f"{RAW_DIR}/07_scheme_performance.csv")

# Convert all return columns to numeric
return_cols = [
    c for c in perf.columns
    if "return" in c.lower()
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Detect expense ratio column automatically
expense_cols = [
    c for c in perf.columns
    if "expense" in c.lower()
]

if len(expense_cols) > 0:

    expense_col = expense_cols[0]

    perf[expense_col] = pd.to_numeric(
        perf[expense_col],
        errors="coerce"
    )

    anomalies = perf[
        (perf[expense_col] < 0.1) |
        (perf[expense_col] > 2.5)
    ]

    print("\nExpense Ratio Anomalies:", len(anomalies))

perf = perf.drop_duplicates()

perf.to_csv(
    f"{PROCESSED_DIR}/07_scheme_performance.csv",
    index=False
)

print("✓ Scheme performance cleaned")

# ======================================================
# 4. COPY REMAINING DATASETS
# ======================================================

remaining = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("\nCopying remaining datasets...")

for file in remaining:

    df = pd.read_csv(f"{RAW_DIR}/{file}")

    df.to_csv(
        f"{PROCESSED_DIR}/{file}",
        index=False
    )

    print(f"✓ {file}")

print("\n" + "=" * 70)
print("ALL DATASETS CLEANED SUCCESSFULLY")
print("=" * 70)

print("\nSaved cleaned files to:")
print(PROCESSED_DIR)