#  Lecture 3 – String Methods, Datetime Handling, Grouping & Aggregation in Pandas  

##  Learning Objectives
By the end of this lecture, you will be able to:  
- Apply **string operations** on DataFrame columns.  
- Work with **datetime objects** in pandas.  
- Perform **grouping and aggregation**.  
- Extract insights from grouped data.  

---

##  Theory (Explanation)

### 1. String Methods in Pandas  
Pandas provides vectorized string functions through `.str` accessor.  

Examples:  
```python
df['Name'].str.upper()        # Convert to uppercase
df['Name'].str.lower()        # Convert to lowercase
df['Name'].str.contains('a')  # Check if contains 'a'
df['Name'].str.len()          # Length of each string
df['Name'].str.replace('a','@')  # Replace characters
```

### 2. Datetime Handling  
- Convert to datetime:
```python
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
```
- Extract components:
```python
df['Year'] = df['JoinDate'].dt.year
df['Month'] = df['JoinDate'].dt.month
df['Day'] = df['JoinDate'].dt.day
```
- Date filtering:
```python
df[df['JoinDate'] > '2023-01-01']
```

### 3. Grouping & Aggregation  
- Group by column:  
```python
df.groupby('City')['Salary'].mean()
```
- Multiple aggregations:  
```python
df.groupby('City').agg({'Salary':['mean','max','min'], 'Age':'median'})
```
- Count per group:  
```python
df['City'].value_counts()
```

---

##  Code Example
```python
import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Kiran'],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai'],
    'Salary': [50000, 60000, 55000, 65000, 60000],
    'JoinDate': ['2022-05-12', '2023-01-20', '2022-11-15', '2023-03-01', '2023-02-10']
}

df = pd.DataFrame(data)

# Convert JoinDate to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print("Original DataFrame:\n", df)

# String operations
print("\nUppercase Names:\n", df['Name'].str.upper())

# Extract year and month
df['Year'] = df['JoinDate'].dt.year
df['Month'] = df['JoinDate'].dt.month

# Grouping
grouped = df.groupby('City')['Salary'].mean()
print("\nAverage Salary by City:\n", grouped)
```

---

##  Practical Tasks (Assignments)

1. Convert all employee names to lowercase.  
2. Extract only the **year** from the `JoinDate` column.  
3. Find the **highest salary** in each city.  
4. Count how many employees joined in **2023**.  
5. Replace the letter `a` in all names with `*`.  
