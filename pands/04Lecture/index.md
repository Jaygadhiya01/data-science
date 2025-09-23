# Lecture 4 : Pandas

## 1. Monthly Sales Trend (Time-Series Analysis)

Real-world sales analysis often looks at month-by-month performance.

``` python
import pandas as pd

df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract Year & Month
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()

# Monthly sales
monthly_sales = df.groupby(["Year", "Month"])["Sales"].sum()
print(monthly_sales)

# Visualization
monthly_sales.plot(kind="bar", title="Monthly Sales Trend")
```

**Variations:**

``` python
# Group by year-month
df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()

# Find best and worst sales months
```

------------------------------------------------------------------------

## 2. Pivot Tables & Crosstabs

**Pivot Table (like Excel Pivot):**

``` python
# Total sales by Region & Category
pivot = pd.pivot_table(df,
                       values="Sales",
                       index="Region",
                       columns="Category",
                       aggfunc="sum",
                       fill_value=0)
print(pivot)
```

**Multiple aggregations:**

``` python
pd.pivot_table(df, 
               values=["Sales", "Quantity"], 
               index="Region", 
               columns="Category", 
               aggfunc={"Sales": "sum", "Quantity": "mean"})
```

**Crosstab (frequency tables):**

``` python
# Number of orders by Region & Category
ct = pd.crosstab(df["Region"], df["Category"])
print(ct)
```

**Difference:** - `pivot_table()` → numerical aggregation (sum, mean,
etc.) - `crosstab()` → frequency counts

------------------------------------------------------------------------

## 3. Exporting Data

After cleaning/analysis, results are often exported for reporting.

``` python
# Export cleaned data
df.to_csv("cleaned_sales.csv", index=False)

# Export to Excel
df.to_excel("sales_report.xlsx", sheet_name="Report", index=False)

# Export pivot table
pivot.to_csv("pivot_sales.csv")

# Export to JSON
df.to_json("sales.json", orient="records", lines=True)
```

------------------------------------------------------------------------

## 4. Basic Visualization with Pandas

Pandas integrates with Matplotlib for quick visualizations.

``` python
# Line Plot
df.groupby("Date")["Sales"].sum().plot(kind="line", title="Daily Sales Trend")

# Bar Chart
df.groupby("Region")["Sales"].sum().plot(kind="bar", title="Sales by Region")

# Pie Chart
df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")

# Histogram
df["Sales"].plot(kind="hist", bins=10, title="Sales Distribution")

# Scatter Plot
df.plot(kind="scatter", x="Quantity", y="Sales", title="Sales vs Quantity")
```

------------------------------------------------------------------------

## 5. Summary

-   **Monthly Sales Trend** → Analyze & visualize sales by time.\
-   **Pivot Tables** → Summarize data (like Excel).\
-   **Crosstabs** → Frequency tables.\
-   **Exporting Data** → CSV, Excel, JSON for reporting.\
-   **Visualization** → Line, bar, pie, histogram, scatter.

------------------------------------------------------------------------

## 6. Pandas Workflow

**Load → Clean → Transform → Analyze → Export → Visualize**
