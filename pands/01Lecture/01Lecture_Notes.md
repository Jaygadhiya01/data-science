#  Lecture 4 -- Introduction to Pandas: DataFrame, Methods, and Attributes

##  Learning Objectives

By the end of this lecture, students will be able to:\
- Understand what **Pandas** is and why it is widely used in data
analysis.\
- Explain what a **DataFrame** is.\
- Create a **DataFrame** using different approaches.\
- Use important **methods** (functions) and **attributes** (properties)
of DataFrames.

------------------------------------------------------------------------

##  1. Introduction to Pandas

-   **Pandas** is an open-source Python library built on top of
    **NumPy**.\
-   It is used for **data manipulation, analysis, and cleaning**.\
-   Provides two main data structures:
    -   **Series**: One-dimensional labeled array (like a column in
        Excel).\
    -   **DataFrame**: Two-dimensional labeled data structure (like an
        Excel sheet or SQL table).

------------------------------------------------------------------------

##  2. What is a DataFrame?

-   A **DataFrame** is a **2D table** of data with labeled rows and
    columns.\
-   It is similar to a spreadsheet or SQL table.\
-   Columns can have **different data types** (int, float, string,
    etc.).

**Example:**

  Name    Age   City
  ------- ----- -----------
  Amit    22    Delhi
  Riya    25    Mumbai
  Karan   28    Bangalore

------------------------------------------------------------------------

##  3. How to Create a DataFrame

Pandas provides multiple ways to create a DataFrame:

### (a) From a Dictionary

``` python
import pandas as pd  

data = {  
    'Name': ['Amit', 'Riya', 'Karan'],  
    'Age': [22, 25, 28],  
    'City': ['Delhi', 'Mumbai', 'Bangalore']  
}  

df = pd.DataFrame(data)  
print(df)
```

### (b) From a List of Lists

``` python
data = [  
    ['Amit', 22, 'Delhi'],  
    ['Riya', 25, 'Mumbai'],  
    ['Karan', 28, 'Bangalore']  
]  

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])  
print(df)
```

### (c) From a CSV File

``` python
df = pd.read_csv('students.csv')  
print(df.head())  
```

------------------------------------------------------------------------

##  4. Important DataFrame Attributes

Attributes are like **properties** (no `()` needed).

  ----------------------------------------------------------------------------------------------------
  Attribute               Description                 Example
  ----------------------- --------------------------- ------------------------------------------------
  `df.shape`              Returns (rows, columns)     `(3, 3)`

  `df.columns`            Column names                `Index(['Name','Age','City'], dtype='object')`

  `df.index`              Row index                   `RangeIndex(start=0, stop=3, step=1)`

  `df.dtypes`             Data types of columns       `object, int64`

  `df.values`             Numpy array of data         `array([...])`

  `df.head()`             First 5 rows                `df.head(2)` → first 2 rows

  `df.tail()`             Last 5 rows                 `df.tail(2)` → last 2 rows
  ----------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

##  5. Important DataFrame Methods

Methods are like **functions** (use `()`).

  --------------------------------------------------------------------------------
  Method                      Description                    Example
  --------------------------- ------------------------------ ---------------------
  `df.info()`                 Summary of DataFrame           Column types & null
                                                             values

  `df.describe()`             Statistics for numeric columns Mean, Min, Max, etc.

  `df.sort_values('Age')`     Sort by column                 Sorts by Age

  `df['Age'].mean()`          Find mean of a column          Average age

  `df.drop('City', axis=1)`   Drop column                    Removes `City`

  `df.drop(0)`                Drop row by index              Removes row 0

  `df.isnull().sum()`         Missing values check           Count nulls
  --------------------------------------------------------------------------------

------------------------------------------------------------------------

##  6. Summary

-   Pandas is a **powerful data analysis library**.\
-   A **DataFrame** is a 2D labeled data structure.\
-   You can create DataFrames from **dictionaries, lists, CSV/Excel
    files, etc.**\
-   **Attributes** help explore structure (`shape`, `columns`,
    `dtypes`).\
-   **Methods** help manipulate/analyze data (`info()`, `describe()`,
    `sort_values()`).




### Task: DataFrame Methods

- On the students DataFrame:

    - Find the average marks.
    - Sort the DataFrame by Age.
    - Drop the Marks column.
    - Drop the first row.
    - Check if any column has missing values.
