import pandas as pd
import os

DATA_DIR = "data/raw"

csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]

summary = []

for file in sorted(csv_files):

    path = os.path.join(DATA_DIR, file)

    print("\n" + "="*80)
    print(f"DATASET: {file}")
    print("="*80)

    df = pd.read_csv(path)

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nHead")
    print(df.head())

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    print("\nMissing Values:", missing)
    print("Duplicate Rows:", duplicates)

    summary.append([
        file,
        df.shape[0],
        df.shape[1],
        missing,
        duplicates
    ])

summary_df = pd.DataFrame(
    summary,
    columns=[
        "dataset",
        "rows",
        "columns",
        "missing_values",
        "duplicates"
    ]
)

summary_df.to_csv(
    "reports/data_quality_summary.csv",
    index=False
)

print("\nSaved reports/data_quality_summary.csv")