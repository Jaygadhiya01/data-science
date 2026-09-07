
# Day 3 — Datetime & Resampling (transactions_day3.csv)

**Your Goals:**
1) Parse `timestamp` to datetime; set as index.
2) Create features: `date`, `hour`, `dow` (0=Mon).
3) Total revenue per day; which day had the highest revenue?
4) Revenue by `channel` and `city` (pivot table).
5) Rolling 3-day revenue mean; plot daily revenue and rolling mean on the same chart.
6) Bucket hours into `Morning(5-11)`, `Afternoon(12-17)`, `Evening(18-22)`, `Night(23-4)` and compare average basket size.

**Hints:**
- `pd.to_datetime`, `.dt.*`, `.resample('D').sum()`
- `pivot_table(values='amount', index='date', columns='channel', aggfunc='sum')`
- `pd.cut` for time buckets
