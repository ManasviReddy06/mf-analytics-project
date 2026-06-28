import os
import pandas as pd

RAW = "data/raw/08_investor_transactions.csv"
OUT = "data/processed/08_investor_transactions.csv"

os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("Cleaning Investor Transactions")
print("=" * 60)

df = pd.read_csv(RAW)

print("Rows before cleaning :", len(df))

# -------------------------
# Convert date
# -------------------------
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

df = df.dropna(subset=["transaction_date"])

# -------------------------
# Standardize transaction type
# -------------------------
df["transaction_type"] = (
    df["transaction_type"]
      .astype(str)
      .str.strip()
      .str.upper()
)

mapping = {
    "SYSTEMATIC INVESTMENT PLAN": "SIP",
    "SIP": "SIP",
    "LUMP SUM": "LUMPSUM",
    "LUMPSUM": "LUMPSUM",
    "REDEMPTION": "REDEMPTION"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

# -------------------------
# Amount validation
# -------------------------
df["amount_inr"] = pd.to_numeric(
    df["amount_inr"],
    errors="coerce"
)

df = df[df["amount_inr"] > 0]

# -------------------------
# KYC validation
# -------------------------
df["kyc_status"] = (
    df["kyc_status"]
      .astype(str)
      .str.upper()
      .str.strip()
)

valid = [
    "VERIFIED",
    "PENDING",
    "REJECTED"
]

invalid = ~df["kyc_status"].isin(valid)

print("Invalid KYC rows :", invalid.sum())

df.loc[invalid, "kyc_status"] = "UNKNOWN"

# -------------------------
# Remove duplicates
# -------------------------
df = df.drop_duplicates()

print("Rows after cleaning :", len(df))

df.to_csv(OUT, index=False)

print("\nSaved :", OUT)
