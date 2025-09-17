# . Introduction to CSV Files
# CSV (Comma Separated Values) = Common format for datasets.

# Each row = record (like a student, a transaction, etc.).

# Each column = field (like Name, Age, Marks).

# Example: students.csv

# Name,Age,Marks
# A,18,75
# B,19,82
# C,20,
# D,18,65
# 2. Reading CSV with np.loadtxt
# Use when data is purely numeric (no missing values, no text).

# Example:

import numpy as np

data = np.loadtxt("numbers.csv", delimiter=",", skiprows=1)  # skip header
print("Data:\n", data)
print("Shape:", data.shape)


# 3. Reading CSV with np.genfromtxt
# More flexible → can handle missing values.

# Supports filling missing values with default.

# Example:

data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)
print("Data:\n", data)

# 4. Handling Missing Values
# Replace NaN with 0

data = np.genfromtxt("students.csv", delimiter=",", skip_header=1, filling_values=0)
print("Data with NaN filled as 0:\n", data)
# Replace NaN with Column Mean

data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

marks = data[:,1]  # second column
mean_marks = np.nanmean(marks)
marks = np.nan_to_num(marks, nan=mean_marks)

print("Marks after handling NaN:", marks)

# 5. Selecting Rows and Columns
data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

ages = data[:,0]   # first column
marks = data[:,1]  # second column

print("Ages:", ages)
print("Marks:", marks)
print("Average Marks:", np.nanmean(marks))
print("Top 2 Marks:", np.sort(marks)[-2:])

# 6. Saving Arrays to CSV
# Use np.savetxt()


arr = np.array([[1, 90], [2, 85], [3, 95]])
np.savetxt("output.csv", arr, delimiter=",", fmt="%d", header="ID,Marks", comments='')
print("Data saved to output.csv")




sales = np.genfromtxt("sales.csv", delimiter=",", skip_header=1)

quantity = sales[:,1]
price = sales[:,2]

# Handle NaN in price
mean_price = np.nanmean(price)
price = np.nan_to_num(price, nan=mean_price)

# Total sales for each row
total_sales = quantity * price
print("Total Sales per product:", total_sales)

# Overall total
print("Grand Total Sales:", np.sum(total_sales))