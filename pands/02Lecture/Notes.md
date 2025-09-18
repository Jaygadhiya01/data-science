Lecture 2 – DataFrame Operations & Data Cleaning in Pandas

## Learning Objectives
By the end of this lecture, you will be able to:
 Select rows and columns in different ways.
 Filter and sort data.
 Add or remove columns.
 Handle missing values (NaN).
 Remove duplicates.
 Convert column data types.

1. Accessing Columns
# Single column
print(df["Product"])

# Multiple columns
print(df[["Product", "Price"]])

2. Accessing Rows
# Single row
print(df.loc[0])     # by label
print(df.iloc[0])    # by position

# Multiple rows
print(df.loc[0:2])

3. Filtering Data
# Price > 10000
print(df[df["Price"] > 10000])

# Electronics only
print(df[df["Category"] == "Electronics"])

# Multiple conditions
print(df[(df["Category"] == "Accessories") & (df["Quantity"] > 5)])

4. Sorting Data
# Sort by Price
print(df.sort_values(by="Price"))

# Sort by Total (highest first)
print(df.sort_values(by="Total", ascending=False))

5. Adding & Deleting Columns
# Add Profit column
df["Profit"] = df["Total"] * 0.10

# Drop Date column
df = df.drop("Date", axis=1)

6. Indexing
# Default index
print(df.index)

# Set OrderID as index
df = df.set_index("OrderID")

# Reset to default
df = df.reset_index()

7. Data Cleaning
(a) Handling Missing Values
# Detect missing values
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# Fill missing values with a constant
df["Price"].fillna(0, inplace=True)

# Fill missing with mean
df["Price"].fillna(df["Price"].mean(), inplace=True)

(b) Handling Duplicates
# Check duplicates
print(df.duplicated().sum())

# Drop duplicates
df = df.drop_duplicates()

(c) Handling Data Types
# Check data types
print(df.dtypes)

# Convert Price to float
df["Price"] = df["Price"].astype(float)

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

8. Hands-on Example
# 1. Drop duplicates if any
df = df.drop_duplicates()

# 2. Fill missing Quantity with average
df["Quantity"].fillna(df["Quantity"].mean(), inplace=True)

# 3. Convert Region to category type
df["Region"] = df["Region"].astype("category")

print(df.info())

## Summary

Select rows/columns → [], .loc[], .iloc[].

Filter and sort → df[condition], sort_values().

Add/remove columns easily.

Data Cleaning → handle NaN, remove duplicates, fix types.