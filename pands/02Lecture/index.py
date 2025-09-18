import pandas as pd


df = pd.read_csv('sales.csv')  
print(df) 

# print(df["product"])


# print(df[["Product", "Price"]])


# print(df.loc[0])     # by label
# print(df.iloc[0])    # by position


# print(df.loc[0:5])



# print(df[df["Price"] > 20000])


# print(df[df["Category"] == "Electronics"])
# print(df[(df["Category"] == "Accessories") & (df["Quantity"] > 2)])

# df["Profit"] = df["Total"] * 0.10

# df = df.drop("Date", axis=1)


# print(df.index)

# df = df.set_index("OrderID")

# print(df)
# df = df.reset_index()
# print(df)


# print(df.isnull())
# print(df.isnull().sum())



# df_cleaned = df.dropna()
 
# print(df)
# print(df_cleaned)



# print(df.duplicated())
# print(df.duplicated().sum())


# df = df.set_index("OrderID")
# print(df)

# df = df.drop_duplicates()
 
# print(df)
