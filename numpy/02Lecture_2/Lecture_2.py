import numpy as np

data = np.array([10, 20, np.nan, 40, 50])
print("Original:", data)

# Check missing values
print("Is NaN:", np.isnan(data))

# Replace NaN with 0
print("NaN to 0:", np.nan_to_num(data))

# Replace NaN with mean
mean_val = np.nanmean(data)
data[np.isnan(data)] = mean_val
print("NaN replaced with mean:", data)



# find mean median std var

scores = np.array([45, 60, 72, 88, 53, 95, 70])
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))
print("Variance:", np.var(scores))
print("90th Percentile:", np.percentile(scores, 90))


# Conditional Filtering with np.where

marks = np.array([35, 78, 62, 90, 49])
result = np.where(marks >= 40, "Pass", "Fail")
print(result)


# Sorting & Unique Values

arr = np.array([5, 2, 7, 2, 8, 5, 9])
print("Sorted:", np.sort(arr))
print("Indices of sorted:", np.argsort(arr))
print("Unique values:", np.unique(arr))



# Broadcasting for Normalization
# Data needs to be scaled (normalized) before analysis.

# Formula:

# X_norm = (X - X_min) / (X_max - X_min)
# Example:

data = np.array([10, 20, 30, 40, 50])
norm_data = (data - data.min()) / (data.max() - data.min())
print("Normalized:", norm_data)



#  Real Dataset Example (CSV)

data=np.genfromtxt("student.csv",deletechars=",",skip_header=1)
print(data)

# Handle NaN in Marks
marks = data[:,1]
mean_marks = np.nanmean(marks)
marks = np.nan_to_num(marks, nan=mean_marks)

print("Marks after handling NaN:", marks)

# Stats
print("Average Marks:", np.mean(marks))
print("Top 3 Marks:", np.sort(marks)[-3:])



