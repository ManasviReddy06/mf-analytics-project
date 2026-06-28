-- 1. Top 5 Funds by AUM

SELECT scheme_name,
       aum_crore
FROM "07_scheme_performance"
ORDER BY aum_crore DESC
LIMIT 5;

---------------------------------------------------

-- 2. Average NAV per Month

SELECT
strftime('%Y-%m',date) Month,
AVG(nav) Avg_NAV
FROM "02_nav_history"
GROUP BY Month;

---------------------------------------------------

-- 3. Transactions by State

SELECT
state,
COUNT(*) Transactions
FROM "08_investor_transactions"
GROUP BY state
ORDER BY Transactions DESC;

---------------------------------------------------

-- 4. Expense Ratio below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM "07_scheme_performance"
WHERE expense_ratio_pct<1;

---------------------------------------------------

-- 5. Top 10 Returns (5 Year)

SELECT
scheme_name,
return_5yr_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 10;

---------------------------------------------------

-- 6. Average Alpha

SELECT
AVG(alpha)
FROM "07_scheme_performance";

---------------------------------------------------

-- 7. Average Sharpe Ratio

SELECT
AVG(sharpe_ratio)
FROM "07_scheme_performance";

---------------------------------------------------

-- 8. Benchmark Average

SELECT
AVG(benchmark_3yr_pct)
FROM "07_scheme_performance";

---------------------------------------------------

-- 9. Total Transactions

SELECT
COUNT(*)
FROM "08_investor_transactions";

---------------------------------------------------

--10. Fund Count by Category

SELECT
category,
COUNT(*)
FROM "01_fund_master"
GROUP BY category;