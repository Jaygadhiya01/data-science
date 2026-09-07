create database sales_analysis;

use sales_analysis;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


INSERT INTO customers (name, email, city, country) VALUES
('Amit Shah', 'amit@example.com', 'Ahmedabad', 'India'),
('Priya Mehta', 'priya@example.com', 'Mumbai', 'India'),
('Ravi Patel', 'ravi@example.com', 'Surat', 'India'),
('Sara Khan', 'sara@example.com', 'Delhi', 'India'),
('John Doe', 'john@example.com', 'New York', 'USA'),
('Emma Brown', 'emma@example.com', 'Sydney', 'Australia'),
('Mike Ross', 'mike@example.com', 'London', 'UK'),
('Rajesh Kumar', 'rajesh@example.com', 'Chennai', 'India'),
('Liam Smith', 'liam@example.com', 'Toronto', 'Canada'),
('Ananya Singh', 'ananya@example.com', 'Pune', 'India');


INSERT INTO orders (customer_id, product_name, quantity, price, order_date) VALUES
(1, 'Laptop', 1, 700, '2024-01-15'),
(2, 'Phone', 2, 300, '2024-02-10'),
(3, 'Tablet', 3, 150, '2024-03-05'),
(4, 'Headphones', 1, 80, '2024-04-12'),
(5, 'Monitor', 2, 250, '2024-05-20'),
(1, 'Keyboard', 5, 50, '2024-06-11'),
(6, 'Mouse', 6, 30, '2024-07-01'),
(7, 'Chair', 2, 120, '2024-08-18'),
(8, 'Desk', 1, 500, '2024-09-22'),
(9, 'Printer', 1, 200, '2024-10-10'),
(10, 'Camera', 2, 600, '2024-11-15'),
(2, 'Smartwatch', 1, 400, '2024-12-01'),
(3, 'Speaker', 2, 100, '2024-06-05'),
(4, 'Router', 1, 60, '2024-07-12'),
(5, 'Hard Drive', 3, 90, '2024-03-19'),
(6, 'USB Cable', 10, 10, '2024-05-08'),
(7, 'Lamp', 2, 45, '2024-04-25'),
(8, 'Notebook', 5, 20, '2024-02-14'),
(9, 'Pen', 12, 5, '2024-01-30'),
(10, 'Backpack', 1, 70, '2024-09-05');


SELECT * FROM orders WHERE price > 500;

SELECT * FROM customers WHERE country = 'India';


SELECT *, (quantity * price) AS total_price FROM orders ORDER BY total_price DESC LIMIT 5;

SELECT * FROM orders WHERE YEAR(order_date) = 2024;


SELECT * FROM orders WHERE quantity > 5 AND price < 1000;

SELECT c.name, SUM(o.quantity * o.price) AS total_sales FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;

SELECT c.name, COUNT(o.order_id) AS total_orders FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;

SELECT c.name AS customer_name, o.product_name, o.quantity, o.price FROM customers c JOIN orders o ON c.customer_id = o.customer_id;

SELECT c.name, SUM(o.quantity * o.price) AS total_revenue FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;

SELECT c.name FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id WHERE o.order_id IS NULL;

SELECT * FROM orders WHERE (quantity * price) > (SELECT AVG(quantity * price) FROM orders);

SELECT c.name FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name HAVING SUM(o.quantity * o.price) > (SELECT AVG(quantity * price) FROM orders);

SELECT c.name, SUM(o.quantity * o.price) AS total_spent FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name ORDER BY total_spent DESC LIMIT 3;


SELECT product_name, SUM(quantity) AS total_ordered FROM orders GROUP BY product_name ORDER BY total_ordered DESC LIMIT 1;

SELECT c.city, SUM(o.quantity * o.price) AS city_sales FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.city;

SELECT COUNT(DISTINCT product_name) AS unique_products FROM orders;

SELECT MONTH(order_date) AS month, SUM(quantity * price) AS monthly_sales FROM orders GROUP BY MONTH(order_date) ORDER BY monthly_sales DESC LIMIT 1;

SELECT c.name, COUNT(o.order_id) AS orders_count FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name HAVING orders_count > 3;

SELECT c.name FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name HAVING COUNT(DISTINCT o.product_name) > 1;

SELECT o.customer_id, o.order_date, SUM(o.quantity * o.price) OVER (PARTITION BY o.customer_id ORDER BY o.order_date) AS cumulative_sales FROM orders o ORDER BY o.customer_id, o.order_date;

SELECT c.name,SUM(o.quantity * o.price) AS customer_sales, (SUM(o.quantity * o.price) / (SELECT SUM(quantity * price) FROM orders)) * 100 AS percentage_of_total FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;

SELECT c.name FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.order_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) WHERE o.order_id IS NULL;

SELECT c.city, AVG(o.quantity * o.price) AS avg_order_value FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.city ORDER BY avg_order_value DESC LIMIT 5;

CREATE OR REPLACE VIEW customer_total_purchase AS SELECT c.name, SUM(o.quantity * o.price) AS total_purchase FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;

DELIMITER $$

CREATE PROCEDURE total_sales_between_dates(IN start_date DATE, IN end_date DATE)
BEGIN
    SELECT SUM(quantity * price) AS total_sales
    FROM orders
    WHERE order_date BETWEEN start_date AND end_date;
END$$

DELIMITER ;

CALL total_sales_between_dates('2024-01-01', '2024-12-31');


CREATE TABLE order_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_log (order_id) VALUES (NEW.order_id);
END$$

DELIMITER ;











SELECT c.country,
       SUM(o.quantity * o.price) AS total_sales,
       AVG(o.quantity * o.price) AS avg_sales,
       COUNT(DISTINCT c.customer_id) AS num_customers
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.country;






