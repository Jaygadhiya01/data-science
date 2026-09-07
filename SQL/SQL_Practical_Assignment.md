# SQL Practical Assignment – Clauses Practice

## Database Creation
```sql
CREATE DATABASE CompanyDB;
USE CompanyDB;
```

## Create Table: EmployeeData
```sql
CREATE TABLE EmployeeData (
    empId INT PRIMARY KEY,
    empName VARCHAR(50),
    empAge INT,
    empSalary DECIMAL(10,2),
    empDepartment VARCHAR(50),
    empCountry VARCHAR(50)
);
```

## Insert Sample Data
```sql
INSERT INTO EmployeeData VALUES
(1, 'Rahul', 28, 40000, 'Sales', 'India'),
(2, 'Sneha', 32, 50000, 'HR', 'India'),
(3, 'Vikas', 26, 35000, 'Sales', 'India'),
(4, 'Anita', 29, 42000, 'IT', 'India'),
(5, 'Rohan', 31, 47000, 'Sales', 'India'),
(6, 'Priya', 27, 39000, 'Finance', 'India'),
(7, 'Karan', 35, 55000, 'Sales', 'India'),
(8, 'Divya', 25, 36000, 'IT', 'India'),
(9, 'Manish', 30, 48000, 'Sales', NULL),
(10, 'Pooja', 28, 40000, 'Marketing', NULL);
```

## SQL Tasks

### Task 1
Display all employee details whose salary is greater than 40000.

### Task 2
Show the name and department of employees who are from the Sales department.

### Task 3
List the employees whose name starts with 'A' and age is less than 30.

### Task 4
Display the unique departments available in the company.

### Task 5
Show the top 3 highest-paid employees.

### Task 6
Display all employees sorted by salary in descending order.

### Task 7
Find the average salary of each department.

### Task 8
Display only those departments where the average salary is more than 45000. (Use GROUP BY and HAVING)

### Task 9
Count the number of employees in each department.

### Task 10
Show the minimum and maximum salary in each department.

### Task 11
Find the total salary of all employees except those from the HR department.

### Task 12
Display employee details where country is NULL or not mentioned.

### Task 13
Show employees whose department name contains the letter 'e'.

### Task 14
Display employees with a salary between 30000 and 50000.

### Task 15
Show all employees who do not belong to the Sales or IT department.
