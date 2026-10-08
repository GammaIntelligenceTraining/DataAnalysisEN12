-- ==============================================================================
-- Lesson 4 Capstone Project: Nexus Retail Architecture & Fixtures
-- Run this script to establish the database, populate initial records, and
-- review the complete roadmap of analytical, view, and debugging tasks.
--
-- PROJECT ROADMAP:
--   Phase 1: DDL — Normalized Relational Schema Setup
--   Phase 2: DML — Production Fixture Ingestion
--   Phase 3: Analytical SQL Pipeline (Tasks 1 - 5)
--   Phase 4: Encapsulation with Business Views (Tasks 6 - 8)
--   Phase 5: Live Debugging & Edge-Case Troubleshooting (Tasks 9 - 13)
-- ==============================================================================

-- 1. Create Clean Project Schema
CREATE SCHEMA IF NOT EXISTS nexus_retail;
USE nexus_retail;

-- 2. Drop existing tables in reverse dependency order
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS customers;

-- 3. Create Entities with Constraints (Phase 1: DDL)
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(50) NOT NULL,
    signup_date DATE NOT NULL,
    loyalty_tier VARCHAR(20) DEFAULT 'Standard'
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    cost_price DECIMAL(8,2) NOT NULL,
    unit_price DECIMAL(8,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    shipping_city VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    line_total DECIMAL(8,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ==============================================================================
-- 4. Ingest Production Fixtures (Phase 2: DML)
-- ==============================================================================

-- Customers
INSERT INTO customers (full_name, email, country, signup_date, loyalty_tier) VALUES
('Marcus Aurelius', 'marcus@rome.org', 'Italy', '2023-01-10', 'VIP'),
('Ada Lovelace', 'ada@computing.co.uk', 'United Kingdom', '2023-02-15', 'VIP'),
('Alan Turing', 'alan@bletchley.co.uk', 'United Kingdom', '2023-03-20', 'Standard'),
('Grace Hopper', 'grace@navy.mil', 'United States', '2023-04-05', 'VIP'),
('Nikola Tesla', 'nikola@wardenclyffe.org', 'Serbia', '2023-05-12', 'Standard'),
('Hedy Lamarr', 'hedy@hollywood.com', 'United States', '2023-06-01', 'Standard');
-- Note: Hedy Lamarr has signed up but never placed an order.

-- Categories
INSERT INTO categories (category_name) VALUES
('Computing'),
('Accessories'),
('Office Furniture'),
('Audio');

-- Products
INSERT INTO products (product_name, category_id, cost_price, unit_price, stock_quantity) VALUES
('Pro Laptop 15', 1, 800.00, 1200.00, 45),
('Mechanical Keyboard', 2, 60.00, 150.00, 120),
('Ergonomic Mesh Chair', 3, 180.00, 350.00, 30),
('Standing Desk Pro', 3, 260.00, 500.00, 15),
('Noise-Cancelling Headphones', 4, 110.00, 250.00, 50),
('Studio USB Microphone', 4, 45.00, 100.00, 0);
-- Note: Studio USB Microphone has 0 stock and has never been ordered.

-- Orders
INSERT INTO orders (customer_id, order_date, shipping_city, status) VALUES
(1, '2024-01-15', 'Rome', 'Delivered'),
(2, '2024-01-20', 'London', 'Delivered'),
(2, '2024-02-10', 'London', 'Delivered'),
(3, '2024-02-14', 'Manchester', 'Cancelled'),
(4, '2024-03-01', 'Washington', 'Delivered'),
(4, '2024-03-20', 'Boston', 'Delivered'),
(5, '2024-03-25', 'Belgrade', 'Pending');

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity, line_total) VALUES
(1, 1, 1, 1200.00),
(1, 2, 2, 300.00),
(2, 3, 1, 350.00),
(3, 4, 1, 500.00),
(3, 5, 2, 500.00),
(4, 2, 1, 150.00), -- Cancelled order
(5, 1, 1, 1200.00),
(6, 2, 2, 300.00),
(6, 5, 1, 250.00),
(7, 3, 1, 350.00); -- Pending order

-- ==============================================================================
-- 5. Project Task Prompts (Phases 3, 4, and 5)
-- Below is the complete list of assignment tasks to be executed on nexus_retail.
-- Reference solutions are documented in teacher_materials.md.
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- PHASE 3: Analytical SQL Pipeline (Business Intelligence)
-- ------------------------------------------------------------------------------

-- Task 1: 3-Table Order Detail Directory
-- Prompt: Write an operational auditing query that joins `orders`, `customers`,
-- `order_items`, and `products` to produce a unified transaction log. Retrieve
-- each order's ID, placement date, customer full name (as `customer_name`),
-- destination country, product name, quantity ordered, line total, and current
-- order status. Order the results by order date in descending order.

-- Task 2: Product Profitability & Margins
-- Prompt: Write a catalog profitability query that joins `products` with `categories`
-- on `category_id` to evaluate merchandise margins across inventory. Select the
-- product name, category name, cost price, and unit price, then compute the dollar
-- profit per unit (`unit_price - cost_price`) as `unit_profit` and the gross profit
-- margin percentage rounded to one decimal place as `profit_margin_pct`. Sort by
-- profit margin percentage descending.

-- Task 3A: Detecting Inactive Registered Customers
-- Prompt: Write a re-engagement marketing query using a `LEFT JOIN` between
-- `customers` and `orders` to detect all registered accounts that have never placed
-- an order. Filter for records where the order ID is `NULL`, returning customer ID,
-- full name, email, and sign-up date.

-- Task 3B: Detecting Ghost Products (Zero-Sales Catalog Items)
-- Prompt: Write an inventory audit query using a `LEFT JOIN` between `products` and
-- `order_items` to identify catalog items that have generated zero historical sales.
-- Filter for records where the order item ID is `NULL`, selecting product ID,
-- product name, and stock quantity.

-- Task 4: Executive Financial Breakdown by Category
-- Prompt: Write an executive departmental performance query joining `categories`,
-- `products`, `order_items`, and `orders` to calculate sales metrics across
-- merchandise departments for fulfilled orders (`status = 'Delivered'`). Group by
-- category name to compute distinct delivered orders, total units sold, gross
-- revenue, and estimated gross profit (revenue minus cost). Sort by gross revenue DESC.

-- Task 5: High-Value VIP Customer Segmentation
-- Prompt: Write a customer segmentation query joining `customers`, `orders`, and
-- `order_items` to isolate high-value VIP shoppers who have generated at least
-- $1,000.00 in completed purchases (`status = 'Delivered'`). Group by customer ID,
-- full name, and loyalty tier, applying a `HAVING total_spend >= 1000.00` filter,
-- sorted by total spend descending.

-- ------------------------------------------------------------------------------
-- PHASE 4: Encapsulation with Business Views
-- ------------------------------------------------------------------------------

-- Task 6: Creating Production Views (KPI & Inventory Alerts)
-- Prompt: Create two reusable views:
--   1. `v_customer_order_kpis`: Aggregate total delivered orders, total delivered spend,
--      and average item spend per customer using `LEFT JOIN` and `IFNULL()`.
--   2. `v_inventory_reorder_alerts`: Join products and categories and evaluate stock
--      thresholds with a `CASE` statement ('OUT OF STOCK', 'LOW STOCK', 'HEALTHY').

-- Task 7: Querying the KPI View
-- Prompt: Query `v_customer_order_kpis` to extract a ranked customer leaderboard
-- sorted by total delivered spend in descending order.

-- Task 8: Querying the Inventory Alert View
-- Prompt: Query `v_inventory_reorder_alerts` to identify all catalog items requiring
-- immediate restocking action (`stock_status <> 'HEALTHY'`).

-- ------------------------------------------------------------------------------
-- PHASE 5: Live Debugging & Edge-Case Troubleshooting
-- ------------------------------------------------------------------------------

-- Task 9: Foreign Key Constraint Violations (Error 1452)
-- Prompt: Test relational integrity enforcement by attempting to insert an order
-- item with an invalid foreign key (`product_id = 999`) into `order_items`. Diagnose
-- Error 1452, query `products` for valid keys, and execute a valid insert (`product_id = 3`).

-- Task 10: Accidental Cartesian Products (Missing Join Condition)
-- Prompt: Demonstrate the performance risk of omitting the `ON` condition by executing
-- a join between `customers` and `orders`. Verify the 42-row Cartesian product, and
-- contrast it with the corrected inner join returning 7 true orders.

-- Task 11: NULL Arithmetic in Aggregations
-- Prompt: Identify calculation errors caused by `NULL` values when aggregating outer
-- joins for customers with zero orders. Implement `IFNULL(SUM(...), 0.00)` to ensure
-- financial calculations output clean numerical zeros.

-- Task 12: Ambiguous Column References (Error 1052)
-- Prompt: Diagnose and fix Error Code 1052 (`Column 'customer_id' in field list is
-- ambiguous`) by qualifying all shared column references with table aliases.

-- Task 13: Filtering Outer Joins in WHERE vs ON Clauses
-- Prompt: Diagnose the subtle logic trap where placing an outer table filter in the
-- `WHERE` clause unintentionally converts a `LEFT JOIN` into an `INNER JOIN`. Fix
-- it by moving the filter condition into the `ON` clause to preserve all customer records.
