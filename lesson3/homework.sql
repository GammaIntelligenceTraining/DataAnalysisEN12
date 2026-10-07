-- Homework Lesson 3: Functions, Aggregations, and Basic Joins
--
-- SETUP SCRIPT: Run this entire block first to create the testing environment.
-- Do not modify the setup code.

CREATE SCHEMA IF NOT EXISTS homework_lesson3;
USE homework_lesson3;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    joined_date DATE NOT NULL
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    total_amount DECIMAL(6,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (first_name, last_name, city, joined_date) VALUES
('Alice', 'Brown', 'New York', '2023-01-15'),
('Bob', 'Smith', 'Chicago', '2023-03-22'),
('Charlie', 'Davis', 'New York', '2023-06-10'),
('Diana', 'Prince', 'Los Angeles', '2023-08-05'),
('Evan', 'Wright', 'Chicago', '2024-01-11'),
('Fiona', 'Gallagher', 'Boston', '2024-02-19'),
('George', 'Clark', 'Seattle', '2024-03-01'),
('Hannah', 'Abbott', 'Boston', '2024-04-14');

INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES
(1, '2024-01-10', 45.00, 'Completed'),
(1, '2024-02-15', 120.50, 'Completed'),
(2, '2024-01-20', 85.00, 'Completed'),
(2, '2024-03-05', 210.00, 'Completed'),
(3, '2024-02-28', 35.00, 'Cancelled'),
(4, '2024-01-18', 310.00, 'Completed'),
(4, '2024-02-22', 95.50, 'Shipped'),
(4, '2024-03-30', 65.00, 'Completed'),
(5, '2024-03-12', 150.00, 'Completed'),
(6, '2024-03-18', 75.00, 'Shipped'),
(6, '2024-04-02', 40.00, 'Completed'),
(1, '2024-04-10', 90.00, 'Completed');
-- Note: Customers 7 (George) and 8 (Hannah) have not placed any orders yet.

-- ==============================================================================
-- ASSIGNMENT TASKS
-- Write your SQL queries below each TODO comment.
-- Only use the concepts covered in Lesson 3:
-- scalar/date functions, aggregate functions, GROUP BY, HAVING, and basic 2-table JOINs.
-- ==============================================================================

-- TODO 1: Aggregate Overview
-- Calculate the total number of orders, the overall sum of total_amount,
-- and the average order amount rounded to 2 decimal places across the entire orders table.
-- Expected output: 1 row with 3 columns (total_orders, total_revenue, avg_order_amount).


-- TODO 2: Filtering and Aggregation
-- Find the minimum order amount and maximum order amount for orders with status = 'Completed'.
-- Expected output: 1 row with 2 columns (min_completed_amount, max_completed_amount).


-- TODO 3: String and Date Scalar Functions
-- Retrieve each customer's full name (first_name and last_name combined with a space),
-- their city in all uppercase letters, and the year they joined using YEAR(joined_date).
-- Expected output: 8 rows with columns: full_name, city_upper, join_year.


-- TODO 4: Date Extraction
-- Find all orders placed in March 2024 using the MONTH() and YEAR() functions on order_date.
-- Expected output: 4 rows (order IDs: 4, 8, 9, 10).


-- TODO 5: Grouping by Category
-- Count how many orders exist for each order status.
-- Expected output: 3 rows showing status and order_count (Completed, Shipped, Cancelled).


-- TODO 6: Grouping by Entity
-- Calculate the total amount spent and the total number of orders placed by each customer_id.
-- Order the results by total_spent in descending order.
-- Expected output: 6 rows (customer IDs: 4, 1, 2, 5, 6, 3).


-- TODO 7: Filtering Groups with HAVING
-- Find all customer IDs whose total spending across all orders is strictly greater than 150.00.
-- Expected output: 4 rows (customer IDs: 4, 1, 2, 5).


-- TODO 8: Basic 2-Table INNER JOIN
-- Join customers and orders to display each order's order_id, order_date, total_amount,
-- and the customer's first_name and last_name.
-- Expected output: 12 rows with 5 columns.


-- TODO 9: INNER JOIN with Aggregation
-- Join customers and orders to display each customer's first_name, last_name,
-- and their total spending (SUM of total_amount).
-- Group by customer_id, first_name, and last_name, and order by total spending descending.
-- Expected output: 6 rows (customers who have placed orders).


-- TODO 10: Basic LEFT JOIN to Detect Inactive Customers
-- Perform a LEFT JOIN from customers to orders to show all customer first_name and last_name,
-- along with their order_id. Filter to display ONLY customers who have NEVER placed an order.
-- Expected output: 2 rows (George Clark, Hannah Abbott).
