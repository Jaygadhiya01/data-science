import pandas as pd  

data = {  
    'Name': ['Amit', 'Riya', 'Karan'],  
    'Age': [22, 25, 28],  
    'City': ['Delhi', 'Mumbai', 'Bangalore']  
}  

df = pd.DataFrame(data)  
print(df)


data = [  
    ['Amit', 22, 'Delhi'],  
    ['Riya', 25, 'Mumbai'],  
    ['Karan', 28, 'Bangalore'],  
    ['Het', 28, 'Ahm']  ,
    ['Niya', 28, 'Surat']  ,
    ['Amit', 22, 'Delhi'],  
    ['Riya', 25, 'Mumbai'],  
    ['Karan', 28, 'Bangalore'],  
    ['Het', 28, 'Ahm']  ,
    ['Niya', 28, 'Surat']  
]  

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'], index=["Row1", "Row2", "Row3", "Row4", "Row5", "Row1", "Row2", "Row3", "Row4", "Row5"] )  
print(df)
print(df.shape)
print(df.size)
print(df.dtypes)
print(df.values)
print(df.head())
print(df.tail())
print(df.describe())
df.info() 



df = pd.read_csv('student.csv')  
print(df)  






# # https://pandas.pydata.org/docs/reference/frame.html


### Task: DataFrame Methods

# - On the students DataFrame:

#     - Find the average marks.
#     - Sort the DataFrame by Age.
#     - Drop the Marks column.
#     - Drop the first row.
#     - Check if any column has missing values.



df = pd.read_csv('student.csv')  
print(df)  

print(df["Marks"])
avg_marks = df["Marks"].mean()
print("Average Marks:", avg_marks)

sorted_df = df.sort_values(by="Age")
print("\nDataFrame sorted by Age:\n", sorted_df)

df_no_marks = df.drop(columns=["Marks"])
print("\nAfter dropping Marks column:\n", df_no_marks)


df_drop_first = df.drop(index=0)
print("\nAfter dropping first row:\n", df_drop_first)

missing_values = df.isnull().any()
print("\nMissing values in each column:\n", missing_values)




