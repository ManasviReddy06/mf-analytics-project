import os
import pandas as pd

RAW = "data/raw/02_nav_history.csv"
OUT = "data/processed/02_nav_history.csv"

os.makedirs("data/processed", exist_ok=True)

print("Loading NAV History...")

df = pd.read_csv(RAW)

print("Rows before cleaning:", len(df))

# Convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["date"])

# Convert NAV
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Remove invalid NAV
df = df[df["nav"] > 0]

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Save
df.to_csv(OUT, index=False)

print("Rows after cleaning :", len(df))
print("Saved :", OUT)