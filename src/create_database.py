import os
import pandas as pd
from sqlalchemy import create_engine

PROCESSED_DIR = "data/processed"

DATABASE = "sqlite:///bluestock_mf.db"

print("=" * 60)
print("Creating SQLite Database")
print("=" * 60)

engine = create_engine(DATABASE)

files = sorted([
    f for f in os.listdir(PROCESSED_DIR)
    if f.endswith(".csv")
])

print(f"\nFound {len(files)} CSV files\n")

for file in files:

    table_name = file.replace(".csv", "")

    print(f"Loading {file}")

    df = pd.read_csv(
        os.path.join(PROCESSED_DIR, file)
    )

    print(f"Rows : {len(df)}")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✓ Loaded into table {table_name}\n")

print("=" * 60)
print("Database Created Successfully!")
print("=" * 60)