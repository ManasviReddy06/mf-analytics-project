import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Fund Master Codes :", len(master_codes))
print("NAV History Codes :", len(nav_codes))
print("Missing Codes     :", len(missing_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes validated successfully.")
else:
    print("\nMissing AMFI Codes:")
    print(sorted(list(missing_codes)))