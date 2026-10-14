-- Homework Lesson 5: Advanced Analytics & Window Functions
--
-- SETUP SCRIPT: Run this entire block first to create the testing environment.
-- Do not modify the setup code.

CREATE SCHEMA IF NOT EXISTS homework_lesson5;
USE homework_lesson5;

DROP TABLE IF EXISTS monthly_sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE monthly_sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    sale_month DATE NOT NULL,
    units_sold INT NOT NULL,
    revenue DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO categories (category_name) VALUES
('Electronics'),
('Accessories'),
('Furniture');

INSERT INTO products (product_name, category_id, unit_price, stock_quantity) VALUES
('Flagship Smartphone', 1, 999.00, 50),
('Mid-range Smartphone', 1, 499.00, 80),
('Budget Smartphone', 1, 199.00, 100),
('Noise-Cancelling Headphones', 2, 299.00, 40),
('Wireless Earbuds', 2, 149.00, 90),
('Bluetooth Speaker', 2, 149.00, 60),
('Ergonomic Office Chair', 3, 350.00, 25),
('Standing Desk Pro', 3, 600.00, 15),
('Bookshelf Modern', 3, 200.00, 30);

INSERT INTO monthly_sales (product_id, sale_month, units_sold, revenue) VALUES
(1, '2024-01-01', 20, 19980.00),
(1, '2024-02-01', 25, 24975.00),
(1, '2024-03-01', 18, 17982.00),
(1, '2024-04-01', 30, 29970.00),
(1, '2024-05-01', 22, 21978.00),
(1, '2024-06-01', 35, 34965.00),
(4, '2024-01-01', 15, 4485.00),
(4, '2024-02-01', 18, 5382.00),
(4, '2024-03-01', 22, 6578.00),
(4, '2024-04-01', 20, 5980.00),
(4, '2024-05-01', 25, 7475.00),
(4, '2024-06-01', 28, 8372.00);

-- ==============================================================================
-- ASSIGNMENT TASKS
-- Write your SQL queries below each TODO comment.
-- Apply the concepts from Lesson 5:
-- Window Functions (OVER, PARTITION BY, ROW_NUMBER, RANK, DENSE_RANK,
-- SUM/AVG OVER, LAG, LEAD).
-- ==============================================================================

-- TODO 1: Global vs. Product Price Benchmark (OVER())
-- Join products and categories to list each product's product_name, category_name,
-- and unit_price, alongside:
--   - the overall average unit price of all catalog products rounded to 2 decimal places (as catalog_avg_price)
--   - the price difference from the catalog average (unit_price - catalog_avg_price as diff_from_catalog_avg)
-- Order by unit_price descending.
-- Expected output: 9 rows showing each product compared to the overall catalog average (399.22).


-- TODO 2: Category Partition Benchmark (PARTITION BY)
-- Join products and categories to retrieve each product's product_name, category_name,
-- and unit_price, alongside:
--   - the average unit price for its specific category rounded to 2 decimal places (as category_avg_price)
--   - the price difference from its category average (unit_price - category_avg_price as diff_from_category_avg)
-- Order by category_name, unit_price descending.
-- Expected output: 9 rows showing product prices compared to their category benchmarks.


-- TODO 3: The Ranking Suite on Tied Records (ROW_NUMBER, RANK, DENSE_RANK)
-- For products in 'Accessories' (category_id = 2), demonstrate how ties are handled.
-- Select product_name, unit_price, and compute all three ranking functions:
--   - ROW_NUMBER() ordered by unit_price DESC as row_num
--   - RANK() ordered by unit_price DESC as rnk
--   - DENSE_RANK() ordered by unit_price DESC as dense_rnk
-- Expected output: 3 rows (Notice how Wireless Earbuds and Bluetooth Speaker tie at 149.00).


-- TODO 4: Filtering Top-N Products per Category (Subquery Filter)
-- Using a subquery, assign a DENSE_RANK() to all products partitioned by category_id
-- and ordered by unit_price descending.
-- Filter the outer query to return strictly the Top 2 most expensive products in each category (price_rank <= 2).
-- Select category_name, product_name, unit_price, and price_rank.
-- Order by category_name, price_rank ascending.
-- Expected output: 6 rows (Top 2 from Electronics, Top 2 from Accessories, Top 2 from Furniture).


-- TODO 5: Cumulative Sales Revenue (Running Total)
-- For product_id = 1, retrieve sale_month, units_sold, revenue, and calculate
-- the cumulative running total of revenue across the months as cumulative_revenue
-- using SUM(revenue) OVER (PARTITION BY product_id ORDER BY sale_month).
-- Order chronologically by sale_month.
-- Expected output: 6 rows showing revenue accumulating from 19,980.00 to 149,850.00.


-- TODO 6: Expanding Running Average Revenue
-- For product_id = 1, calculate the expanding running average of monthly revenue
-- rounded to 2 decimal places as running_avg_revenue using AVG(revenue) OVER (...).
-- Retrieve sale_month, revenue, and running_avg_revenue ordered chronologically by sale_month.
-- Expected output: 6 rows showing monthly revenue alongside the progressive average revenue.


-- TODO 7: Month-over-Month Growth with LAG()
-- For product_id = 1, compare each month's revenue with the previous month's revenue
-- using LAG(revenue, 1, 0.00).
-- Retrieve sale_month, revenue as current_month_revenue, previous_month_revenue,
-- and calculate the monthly growth (current_month_revenue - previous_month_revenue as monthly_growth).
-- Order chronologically by sale_month.
-- Expected output: 6 rows (Row 1 previous revenue 0.00, Row 2 growth +4,995.00, Row 3 growth -6,993.00, etc.).


-- TODO 8: Next Month Volume Projection with LEAD()
-- For product_id = 4, look ahead to the next month's units sold using LEAD(units_sold, 1, 0).
-- Retrieve sale_month, units_sold as current_units_sold, next_units_sold,
-- and calculate the volume change (next_units_sold - current_units_sold as units_projected_change).
-- Order chronologically by sale_month.
-- Expected output: 6 rows (Row 1 shows current 15, next 18, change +3; Row 6 shows next 0, change -28).
