import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
""")

tables = cursor.fetchall()

print("=" * 60)
print("TABLES IN DATABASE")
print("=" * 60)

for table in tables:
    table_name = table[0]

    count = pd.read_sql(
        f"SELECT COUNT(*) AS rows FROM '{table_name}'",
        conn
    )

    print(f"{table_name:<30} {count.iloc[0,0]} rows")

conn.close()

print("\nDatabase verification completed successfully.")
