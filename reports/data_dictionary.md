# Bluestock Mutual Fund Data Dictionary

## 01_fund_master

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| scheme_name | Text | Mutual Fund Scheme |
| fund_house | Text | AMC Name |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |
| plan | Text | Direct / Regular |
| benchmark | Text | Benchmark Index |
| fund_manager | Text | Fund Manager |
| risk_category | Text | Risk Level |

---

## 02_nav_history

| Column | Type |
|---------|------|
| amfi_code | Integer |
| date | Date |
| nav | Float |

---

## 07_scheme_performance

| Column | Type |
|---------|------|
| return_1yr_pct | Float |
| return_3yr_pct | Float |
| return_5yr_pct | Float |
| expense_ratio_pct | Float |
| sharpe_ratio | Float |
| alpha | Float |
| beta | Float |

---

## 08_investor_transactions

| Column | Type |
|---------|------|
| investor_id | Text |
| transaction_date | Date |
| transaction_type | Text |
| amount_inr | Float |
| state | Text |
| city | Text |
| payment_mode | Text |
| kyc_status | Text |

