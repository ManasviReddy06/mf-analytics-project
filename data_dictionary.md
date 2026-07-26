# Data Dictionary

## Project Information

| Field | Value |
|-------|-------|
| Project | Mutual Fund Analytics Platform |
| Company | Bluestock Fintech Pvt. Ltd. |
| Domain | Mutual Fund Analytics |
| Database | SQLite (`bluestock_mf.db`) |
| Dashboard | Microsoft Power BI |
| Prepared By | Manu Reddy |
| Repository | https://github.com/ManasviReddy06/mf-analytics-project |

---

# Overview

This document describes every dataset, table, and field used in the Mutual Fund Analytics Platform. It serves as a reference for understanding the database structure, data types, relationships, and business meaning of each attribute.

---

# Dataset 1 — Fund Master

**File Name**

```
01_fund_master.csv
```

### Description

Contains the master information for all mutual fund schemes used throughout the project.

### Primary Key

```
amfi_code
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| amfi_code | INTEGER | No | Unique AMFI Scheme Code |
| scheme_name | TEXT | No | Name of Mutual Fund Scheme |
| fund_house | TEXT | No | Asset Management Company |
| category | TEXT | No | Fund Category |
| sub_category | TEXT | Yes | Detailed Category |
| expense_ratio | REAL | No | Annual Expense Ratio (%) |
| risk_grade | TEXT | Yes | Risk Classification |
| fund_manager | TEXT | Yes | Fund Manager Name |

---

# Dataset 2 — NAV History

**File Name**

```
02_nav_history.csv
```

### Description

Stores daily historical Net Asset Value (NAV) of every mutual fund.

### Primary Key

```
(amfi_code, date)
```

### Foreign Key

```
amfi_code → Fund Master
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| amfi_code | INTEGER | No | Mutual Fund Scheme Code |
| date | DATE | No | NAV Date |
| nav | REAL | No | Net Asset Value |
| daily_return | REAL | Yes | Daily Return (%) |

---

# Dataset 3 — AUM by Fund House

**File Name**

```
03_aum_by_fund_house.csv
```

### Description

Quarterly Assets Under Management for major Asset Management Companies.

### Primary Key

```
(fund_house, year, quarter)
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| fund_house | TEXT | No | AMC Name |
| year | INTEGER | No | Financial Year |
| quarter | TEXT | No | Quarter |
| aum_crore | REAL | No | Assets Under Management (₹ Crore) |
| number_of_schemes | INTEGER | Yes | Number of Schemes |

---

# Dataset 4 — Monthly SIP Inflows

**File Name**

```
04_monthly_sip_inflows.csv
```

### Description

Industry-wide monthly SIP statistics published by AMFI.

### Primary Key

```
month
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| month | DATE | No | Reporting Month |
| sip_inflow_crore | REAL | No | Monthly SIP Collection |
| active_sip_accounts | REAL | No | Active SIP Accounts |
| new_registrations | INTEGER | Yes | Newly Registered SIPs |
| sip_aum | REAL | Yes | SIP Assets Under Management |

---

# Dataset 5 — Category Inflows

**File Name**

```
05_category_inflows.csv
```

### Description

Monthly inflows by mutual fund category.

### Primary Key

```
(month, category)
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| month | DATE | No | Reporting Month |
| category | TEXT | No | Fund Category |
| net_inflow_crore | REAL | No | Net Inflow (₹ Crore) |

---

# Dataset 6 — Industry Folio Count

**File Name**

```
06_industry_folio_count.csv
```

### Description

Industry-wide folio statistics.

### Primary Key

```
month
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| month | DATE | No | Reporting Month |
| equity_folios | REAL | Yes | Equity Folios |
| debt_folios | REAL | Yes | Debt Folios |
| hybrid_folios | REAL | Yes | Hybrid Folios |
| total_folios | REAL | No | Total Folios |

---

# Dataset 7 — Scheme Performance

**File Name**

```
07_scheme_performance.csv
```

### Description

Stores calculated return and risk metrics for each mutual fund.

### Primary Key

```
amfi_code
```

### Foreign Key

```
amfi_code → Fund Master
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| amfi_code | INTEGER | No | Mutual Fund Scheme Code |
| return_1yr | REAL | No | One-Year Return (%) |
| return_3yr | REAL | No | Three-Year CAGR |
| return_5yr | REAL | Yes | Five-Year CAGR |
| sharpe_ratio | REAL | Yes | Sharpe Ratio |
| sortino_ratio | REAL | Yes | Sortino Ratio |
| alpha | REAL | Yes | Alpha |
| beta | REAL | Yes | Beta |
| max_drawdown | REAL | Yes | Maximum Drawdown |
| standard_deviation | REAL | Yes | Annualized Volatility |

---

# Dataset 8 — Investor Transactions

**File Name**

```
08_investor_transactions.csv
```

### Description

Investor transaction history used for behavioural analysis.

### Primary Key

```
transaction_id
```

### Foreign Key

```
amfi_code → Fund Master
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| transaction_id | INTEGER | No | Unique Transaction ID |
| investor_id | INTEGER | No | Investor Identifier |
| amfi_code | INTEGER | No | Mutual Fund Code |
| transaction_date | DATE | No | Transaction Date |
| transaction_type | TEXT | No | SIP / Lumpsum / Redemption |
| amount | REAL | No | Transaction Amount (₹) |
| age_group | TEXT | Yes | Investor Age Group |
| gender | TEXT | Yes | Investor Gender |
| state | TEXT | Yes | State |
| city_tier | TEXT | Yes | T30 / B30 Classification |
| kyc_status | TEXT | Yes | KYC Verification Status |

---

# Dataset 9 — Portfolio Holdings

**File Name**

```
09_portfolio_holdings.csv
```

### Description

Equity holdings of mutual fund schemes.

### Primary Key

```
(amfi_code, stock_symbol)
```

### Foreign Key

```
amfi_code → Fund Master
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| amfi_code | INTEGER | No | Mutual Fund Code |
| stock_symbol | TEXT | No | NSE/BSE Stock Symbol |
| company_name | TEXT | Yes | Company Name |
| sector | TEXT | No | Industry Sector |
| weight_percentage | REAL | No | Portfolio Weight (%) |
| holding_date | DATE | Yes | Reporting Date |

---

# Dataset 10 — Benchmark Indices

**File Name**

```
10_benchmark_indices.csv
```

### Description

Historical benchmark index values used for fund comparison.

### Primary Key

```
(date, index_name)
```

| Column | Type | Nullable | Description |
|---------|------|----------|-------------|
| date | DATE | No | Trading Date |
| index_name | TEXT | No | Benchmark Index |
| closing_value | REAL | No | Closing Index Value |

---

# Database Relationships

| Parent Table | Child Table | Relationship |
|--------------|------------|--------------|
| Fund Master | NAV History | One-to-Many |
| Fund Master | Scheme Performance | One-to-One |
| Fund Master | Investor Transactions | One-to-Many |
| Fund Master | Portfolio Holdings | One-to-Many |

---

# Database Summary

| Property | Value |
|----------|-------|
| Database Engine | SQLite |
| Database Name | bluestock_mf.db |
| Number of Datasets | 10 |
| Number of Fact Tables | 6 |
| Number of Dimension Tables | 2 |
| Primary Identifier | amfi_code |
| Dashboard Tool | Microsoft Power BI |

---

# Data Sources

The datasets used in this project are obtained from publicly available financial data sources.

| Source | Purpose |
|--------|---------|
| AMFI India | NAV, AUM, SIP, Folios |
| mfapi.in | Historical NAV |
| NSE India | Benchmark Indices |
| BSE India | Market Indices |
| AMFI Monthly Reports | Industry Statistics |

---

# Data Validation

The following validation steps were performed before loading the data into SQLite:

- Removed duplicate records
- Standardized date formats
- Forward-filled missing NAV values where applicable
- Validated AMFI scheme codes
- Verified positive transaction amounts
- Standardized transaction types
- Checked expense ratio ranges
- Verified numeric performance metrics
- Handled missing values
- Enforced consistent data types

---

# Notes

- Monetary values are represented in Indian Rupees (₹).
- All performance metrics were computed using historical NAV data.
- Risk metrics include Sharpe Ratio, Sortino Ratio, Alpha, Beta, Standard Deviation, and Maximum Drawdown.
- The processed datasets serve as the primary data source for the Power BI dashboard.
- This project is intended for educational and portfolio purposes.