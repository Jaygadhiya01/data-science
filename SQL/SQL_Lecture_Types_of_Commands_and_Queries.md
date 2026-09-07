# Lecture: Types of SQL Commands & Basic Database Queries

## 1. Lecture Overview

In this lecture, you will learn about different types of SQL
commands, how to create and manipulate databases and tables, and how to
use `SELECT` and `INSERT` statements. The lecture also includes practice
queries for better understanding.

------------------------------------------------------------------------

## 2. Types of SQL Commands

SQL commands are categorized into five main types based on their
purpose.

  ------------------------------------------------------------------------
  Type        Full Form              Purpose            Example
  ----------- ---------------------- ------------------ ------------------
  DDL         Data Definition        Defines the        CREATE TABLE,
              Language               structure of the   ALTER TABLE, DROP
                                     database (create,  TABLE
                                     alter, drop        
                                     tables).           

  DML         Data Manipulation      Manages data       SELECT, INSERT,
              Language               within tables.     UPDATE, DELETE

  DCL         Data Control Language  Controls access    GRANT, REVOKE
                                     and permissions.   

  TCL         Transaction Control    Manages            COMMIT, ROLLBACK,
              Language               transactions in    SAVEPOINT
                                     the database.      

  DQL         Data Query Language    Retrieves data     SELECT
                                     from databases.    
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Database Related Queries

``` sql
CREATE DATABASE school;
SHOW DATABASES;
USE school;
DROP DATABASE school;
```

------------------------------------------------------------------------

## 4. Table Related Queries

``` sql
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  grade VARCHAR(10)
);

SHOW TABLES;
DESC students;
DROP TABLE students;
```

------------------------------------------------------------------------

## 5. SELECT Command

**Syntax:**

``` sql
SELECT column1, column2 FROM table_name;
```

**Examples:**

``` sql
SELECT * FROM students;
SELECT name, grade FROM students WHERE age > 18;
SELECT DISTINCT grade FROM students;
SELECT name, age FROM students ORDER BY age DESC;
```

------------------------------------------------------------------------

## 6. INSERT Command

**Syntax:**

``` sql
INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
```

**Examples:**

``` sql
INSERT INTO students (student_id, name, age, grade) VALUES (1, 'Amit', 20, 'A');
INSERT INTO students VALUES (2, 'Riya', 19, 'B');
```

------------------------------------------------------------------------

## 7. Practice Questions

1.  Create a database named `college`.
2.  Create a table named `courses` with columns: `course_id`,
    `course_name`, `duration`, `fees`.
3.  Insert 3 records into the `courses` table.
4.  Display all data from the `courses` table.
5.  Display only `course_name` and `fees` of all courses.
6.  Display courses where `fees` \> 20000.
7.  Display courses in ascending order of `duration`.
8.  Delete one record from the `courses` table.
9.  Drop the `courses` table.
10. Drop the `college` database.

------------------------------------------------------------------------

8. Program
``` sql
-- Step 1: Create a Database
CREATE DATABASE school;

-- Step 2: Use the Database
USE school;

-- Step 3: Create a Table
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  grade VARCHAR(10)
);

-- Step 4: Insert Data into the Table
INSERT INTO students (student_id, name, age, grade) VALUES (1, 'Amit', 20, 'A');
INSERT INTO students (student_id, name, age, grade) VALUES (2, 'Riya', 19, 'B');
INSERT INTO students (student_id, name, age, grade) VALUES (3, 'Karan', 21, 'A');
INSERT INTO students (student_id, name, age, grade) VALUES (4, 'Neha', 18, 'C');

-- Step 5: Show All Students
SELECT * FROM students;
```

**Output:**

  student_id   name    age   grade
  ------------ ------- ----- -------
  1            Amit    20    A
  2            Riya    19    B
  3            Karan   21    A
  4            Neha    18    C
