import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")



df["Date"] = pd.to_datetime(df["Date"])

# Extract Year & Month
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()

# Monthly sales
monthly_sales = df.groupby(["Year", "Month"])["Sales"].sum()
print(monthly_sales)

# Visualization
monthly_sales.plot(kind="bar", title="Monthly Sales Trend")

# **Variations:**

# Group by year-month
df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()

# Find best and worst sales months


## 2. Pivot Tables & Crosstabs

# **Pivot Table (like Excel Pivot):**

# Total sales by Region & Category
pivot = pd.pivot_table(df,
                       values="Sales",
                       index="Region",
                       columns="Category",
                       aggfunc="sum",
                       fill_value=0)
print(pivot)

# **Multiple aggregations:**

pd.pivot_table(df, 
               values=["Sales", "Quantity"], 
               index="Region", 
               columns="Category", 
               aggfunc={"Sales": "sum", "Quantity": "mean"})

# **Crosstab (frequency tables):**

# Number of orders by Region & Category
ct = pd.crosstab(df["Region"], df["Category"])
print(ct)

# **Difference:** - 
# `pivot_table()` → numerical aggregation (sum, mean,etc.) 
# `crosstab()` → frequency counts


## 3. Exporting Data

# After cleaning/analysis, results are often exported for reporting.

# Export cleaned data
df.to_csv("cleaned_sales.csv", index=False)

# Export to Excel
df.to_excel("sales_report.xlsx", sheet_name="Report", index=False)

# Export pivot table
pivot.to_csv("pivot_sales.csv")

# Export to JSON
df.to_json("sales.json", orient="records", lines=True)


## 4. Basic Visualization with Pandas

# Pandas integrates with Matplotlib for quick visualizations.

# Line Plot
df.groupby("Date")["Sales"].sum().plot(kind="line", title="Daily Sales Trend")
plt.show()

# Bar Chart
df.groupby("Region")["Sales"].sum().plot(kind="bar", title="Sales by Region")
plt.show()

# Pie Chart
df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.show()

# Histogram
df["Sales"].plot(kind="hist", bins=10, title="Sales Distribution")
plt.show()

# Scatter Plot
df.plot(kind="scatter", x="Quantity", y="Sales", title="Sales vs Quantity")
plt.show()