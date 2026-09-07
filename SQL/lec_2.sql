create database companyDB;


show databases;
use companyDB;

create table emploeedata(empID int primary key ,
empname varchar(20),
empAge int ,
empSalary int,
empDepartment varchar(20),
empCountry varchar(20)
);

create table employee(empID int ,
		empCity varchar(20),
        FOREIGN KEY (empID) REFERENCES emploeedata(empID)
	);
    
INSERT INTO emploeedata (empID, empName, empAge, empSalary, empDepartment, empCountry)
VALUES
(1, 'Amit Sharma', 28, 45000, 'IT', 'India'),
(2, 'Priya Patel', 32, 52000, 'HR', 'India'),
(3, 'Rohan Mehta', 26, 40000, 'Finance', 'India'),
(4, 'Sneha Singh', 29, 47000, 'Marketing', 'India'),
(5, 'Rahul Verma', 35, 60000, 'IT', 'India'),
(6, 'Neha Joshi', 27, 42000, 'Operations', 'India'),
(7, 'Vikas Gupta', 31, 55000, 'Finance', 'India'),
(8, 'Kiran Das', 30, 48000, 'HR', 'India'),
(9, 'Anjali Rao', 25, 39000, 'Marketing', 'India'),
(10, 'Manish Yadav', 33, 58000, 'Operations', 'India');

INSERT INTO employee (empID, empCity)
VALUES
(1, 'Mumbai'),
(2, 'Delhi'),
(3, 'Ahmedabad'),
(4, 'Pune'),
(5, 'Bangalore'),
(6, 'Chennai'),
(7, 'Hyderabad'),
(8, 'Jaipur'),
(9, 'Surat'),
(10, 'Kolkata');


select * from emploeedata;
select * from employee;
update emploeedata set empSalary =empSalary *1.20  where empDepartment ='IT'AND empID > 0;
select * from emploeedata;
SELECT empID, empName, empDepartment, empSalary FROM emploeedata WHERE empDepartment = 'IT';




alter table emploeedata drop column empCountry;


select * from emploeedata;


select emploeedata.empID,emploeedata.empname,employee.empCity from emploeedata,employee;

use companydb;

select * from emploeedata where empSalary>='40000';
select empname,empDepartment from emploeedata where empDepartment ='Marketing';


select * from emploeedata where empname LIKE 'A%'and empAge<'30';

select empDepartment  from emploeedata  group by empDepartment ;

select * from emploeedata order by empSalary DESC limit 3; 

select * from emploeedata order by empSalary desc;

select empDepartment, avg(empSalary) as avg_salary  from emploeedata group by empDepartment;

select empDepartment, avg(empSalary) as avg_salary  from emploeedata group by empDepartment having avg(empSalary)>'45000';


select empDepartment, count(*) as total_employee from emploeedata group by empDepartment ;


SELECT empDepartment, MIN(empSalary) AS min_salary, MAX(empSalary) AS max_salary FROM emploeedata GROUP BY empDepartment;

SELECT SUM(empSalary) AS total_salary FROM emploeedata WHERE empDepartment <> 'HR';

SELECT * FROM emploeedata WHERE empCountry = '';

select * from emploeedata where empDepartment LIKE '%e%';

SELECT * FROM emploeedata WHERE empSalary BETWEEN 30000 AND 50000;


SELECT * FROM emploeedata WHERE empDepartment NOT IN ('Marketing', 'IT');



