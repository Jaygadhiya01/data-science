import pandas as pd


data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Kiran'],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai'],
    'Age' : [25,28,35,42,22],
    'Salary': [50000, 60000, 55000, 65000, 60000],
    'JoinDate': ['2022-05-12', '2023-01-20', '2022-11-15', '2023-03-01', '2023-02-10']
}

df = pd.DataFrame(data)

print(df)
print(df.dtypes)

# Convert JoinDate to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df)
print(df.dtypes)


# String operations
# print("\nUppercase Names:\n", df['Name'].str.upper())
# print("\nUppercase Names:\n", df['Name'].str.lower())
# print("\nUppercase Names:\n", df['Name'].str.title())

# Extract year and month
df['Year'] = df['JoinDate'].dt.year
df['Month'] = df['JoinDate'].dt.month
df['Day'] = df['JoinDate'].dt.day

# print(df['Year'])
# print(df['Month'])
# print(df['Day'])

# Grouping
# grouped = df.groupby('City')['Salary'].mean()
grouped = df.groupby('City')['Salary'].sum()
# print("\nAverage Salary by City:\n", grouped)


multi = df.groupby('City').agg({'Salary':['mean','max','min'], 'Age':'median'})

print(multi)