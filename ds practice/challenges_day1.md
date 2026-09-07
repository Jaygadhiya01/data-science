
# Day 1 — Pandas Essentials (sales_day1.csv)

**Your Goals:**
1) Load the CSV and inspect shape, dtypes, head.
2) Count missing values per column. Which column is messiest?
3) Create a new column `net_sales = units * unit_price * (1 - discount)` and compare with `sales_amount`.
4) Fill missing `units` and `unit_price` with their column medians (copy the DataFrame first!).
5) Drop exact duplicate rows.
6) Filter rows where `region == 'East'` and `net_sales > 1000`.
7) Group by `region` and `product` to get: total units, total net_sales, average discount. Sort by `total net_sales` desc.

**Hints:**
- `df.isna().sum()`, `df.duplicated().sum()`, `df.drop_duplicates()`
- `df.assign(...)` to add columns without mutating
- `groupby([...]).agg({...})`
- Prefer `.median()` over `.mean()` for skewed prices
