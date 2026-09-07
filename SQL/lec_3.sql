CREATE DATABASE Sales_db;

USE Sales_db;

CREATE TABLE customers (
 customer_id int primary key AUTO_INCREMENT,
 name varchar(20),
 email varchar(30),
 city varchar(20),
 country varchar(20)
);

CREATE TABLE products(
	product_id int primary key AUTO_INCREMENT,
    product_name varchar(20),
    category varchar(20),
    price decimal(10,2)
);

CREATE TABLE orders(
	order_id int primary key AUTO_INCREMENT,
    customer_id int,
    order_date date,
    foreign key (customer_id) References customers(customer_id)
);

CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
    
    );
    
INSERT INTO customers (name, email, city, country) VALUES
('Amit Shah', 'amit@example.com', 'Ahmedabad', 'India'),
('John Doe', 'john@example.com', 'New York', 'USA'),
('Priya Mehta', 'priya@example.com', 'Mumbai', 'India'),
('Sara Khan', 'sara@example.com', 'Delhi', 'India'),
('Mike Ross', 'mike@example.com', 'London', 'UK'),
('Ravi Patel', 'ravi@example.com', 'Surat', 'India'),
('Emma Brown', 'emma@example.com', 'Sydney', 'Australia'),
('Rajesh Kumar', 'rajesh@example.com', 'Chennai', 'India'),
('Liam Smith', 'liam@example.com', 'Toronto', 'Canada'),
('Ananya Singh', 'ananya@example.com', 'Pune', 'India');


INSERT INTO products (product_name, category, price) VALUES
('iPhone 15', 'Electronics', 79999),
('Laptop Dell XPS', 'Electronics', 95000),
('Washing Machine', 'Home Appliances', 35000),
('Bluetooth Speaker', 'Electronics', 6000),
('Office Chair', 'Furniture', 8000),
('Dining Table', 'Furniture', 20000),
('LED TV', 'Electronics', 55000),
('Microwave Oven', 'Home Appliances', 15000),
('Refrigerator', 'Home Appliances', 45000),
('Headphones', 'Electronics', 5000);


INSERT INTO orders (customer_id, order_date) VALUES
(1, '2025-06-10'),
(2, '2025-07-05'),
(3, '2025-07-25'),
(4, '2025-08-15'),
(5, '2025-09-01'),
(1, '2025-07-12'),
(6, '2025-08-20'),
(7, '2025-06-30'),
(8, '2025-07-10'),
(9, '2025-07-18');



INSERT INTO order_details (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 10, 2),
(2, 3, 1),
(3, 4, 3),
(4, 2, 1),
(5, 6, 2),
(6, 7, 1),
(7, 8, 1),
(8, 5, 4),
(9, 9, 2);



select name,city from customers;

select city from customers group by city;

SELECT DISTINCT city FROM customers;


select * from products where price>5000;


SELECT * FROM orders WHERE order_date BETWEEN '2025-06-01' AND '2025-08-31';

select * from customers where country ='india';

select * from products order by price desc;


select country ,count(*) as total_customer from customers  group by country;

SELECT SUM(p.price * od.quantity) AS total_sales FROM order_details od JOIN products p ON od.product_id = p.product_id;


SELECT category, AVG(price) AS avg_price FROM products GROUP BY category;


SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);


SELECT DISTINCT c.* FROM customers c JOIN orders o ON c.customer_id = o.customer_id;


SELECT c.* FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id WHERE o.order_id IS NULL;


SELECT c.name, o.order_id FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id;


SELECT c.name, o.order_id, o.order_date FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id;


SELECT p.* FROM products p LEFT JOIN order_details od ON p.product_id = od.product_id WHERE od.product_id IS NULL;

SELECT c.name, o.order_id, o.order_date
FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id
UNION
SELECT c.name, o.order_id, o.order_date
FROM customers c RIGHT JOIN orders o ON c.customer_id = o.customer_id;


SELECT p.product_name, SUM(od.quantity) AS total_sold
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name;


SELECT c.city, SUM(p.price * od.quantity) AS total_sales
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
GROUP BY c.city
ORDER BY total_sales DESC
LIMIT 1;


SELECT c.name, COUNT(o.order_id) AS total_orders FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;


SELECT c.name, SUM(p.price * od.quantity) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 3;


SELECT DISTINCT c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
WHERE p.category = 'Electronics';


SELECT a.name AS customer1, b.name AS customer2, a.country FROM customers a JOIN customers b ON a.country = b.country AND a.customer_id < b.customer_id;


SELECT p.category, SUM(p.price * od.quantity) AS revenue
FROM products p
JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.category
ORDER BY revenue DESC
LIMIT 1;


SELECT c.name, MAX(o.order_date) AS latest_order
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name;


SELECT p.product_name, SUM(od.quantity) AS total_qty
FROM products p
JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_name
HAVING total_qty > 2;

SELECT c.name, o.order_id, SUM(p.price * od.quantity) AS order_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
GROUP BY o.order_id, c.name
ORDER BY order_total DESC
LIMIT 1;


SELECT * FROM customers WHERE name LIKE 'A%';

