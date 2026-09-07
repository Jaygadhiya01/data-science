
# Day 2 — GroupBy & Joins (employees_day2.csv, departments_day2.csv)

**Your Goals:**
1) Read both CSVs; left-join employees with department regions.
2) Compute average and max salary per department.
3) For each department, how many employees joined in each year?
4) Find the top 3 highest-paid employees per department (ties allowed).
5) Detect outliers in `salary` using IQR per department and list them.

**Hints:**
- `pd.merge(employees, departments, on="department", how="left")`
- `df['join_year'] = pd.to_datetime(df['join_date']).dt.year`
- `groupby().agg()` and `nlargest()`
- IQR: `q3 - q1`; outlier if `< q1 - 1.5*IQR` or `> q3 + 1.5*IQR`
