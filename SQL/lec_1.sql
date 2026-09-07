create database student ;

show databases ;
use  student;

create table studnet(studnet_id int primary key ,name varchar(50),age int ,gender varchar(10));

show tables ;
desc studnet;

drop table studnet;
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  grade VARCHAR(10)
);

INSERT INTO students (student_id, name, age, grade) VALUES (1, 'Amit', 20, 'A');
INSERT INTO students VALUES (2, 'Riya', 19, 'B');

select * from students;


create database college;

use college;
create table courses(course_id int primary key,course_name varchar(30), duration varchar(10),fees int);

insert into courses(course_id,course_name,duration,fees)values(1,'python','3 month',30000);
insert into courses values(2,'c++','1 month',10000);
insert into courses values(3,'excl','2 week',5000);

select * from courses;
select course_name,fees from courses;
select course_name,fees from courses  where fees>20000;





use college;


create table student(student_id int,
name varchar(20),
course_id int primary key 
);

create table course(course_id int ,
		course_name varchar(20),
        FOREIGN KEY (course_id) REFERENCES student(course_id)
	);
    
INSERT INTO student (student_id, name, course_id)
VALUES
(1, 'raj', 101),
(2, 'priya', 102),
(3, 'amit', 103),
(4, 'sneha', 104);



INSERT INTO course (course_id, course_name)
VALUES
(101, 'python'),
(102, 'c'),
(103, 'java'),
(104, 'C');


select * from student inner join course on student.course_id=course.course_id;

select * from student as ST inner join course  as CR on ST.course_id=CR.course_id;


select * from student left join course on student.course_id=course.course_id;

select * from student as ST left join course  as CR on ST.course_id=CR.course_id;

select * from student as ST right join course  as CR on ST.course_id=CR.course_id;

select * from student as ST join course  as CR on ST.course_id=CR.course_id;

select * from student as ST left join course  as CR on ST.course_id=CR.course_id union select * from student as ST right join course  as CR on ST.course_id=CR.course_id;




