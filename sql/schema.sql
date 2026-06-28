-- ====================================================
-- Bluestock Mutual Fund Analytics Star Schema
-- ====================================================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    fund_manager TEXT,

    benchmark TEXT,

    risk_category TEXT,

    sebi_category_code TEXT
);

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date DATE,

    day INTEGER,

    month INTEGER,

    quarter INTEGER,

    year INTEGER
);

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date DATE,

    nav REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT,

    amfi_code INTEGER,

    transaction_date DATE,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    expense_ratio_pct REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_house TEXT,

    aum_crore REAL
);
