# Lesson 3 Handout: Functions, Aggregations, and Joins

This guide serves as a quick reference for functions, data summarization, and table joins covered in Lesson 3.

## Aggregate Functions

Aggregate functions perform calculations across multiple rows of data and return a single summary value. Common functions include:
- `COUNT(*)`: Returns the total number of rows.
- `COUNT(column)`: Returns the number of non-NULL values in that column.
- `SUM(column)`: Returns the total sum of numerical values.
- `AVG(column)`: Returns the average of numerical values.
- `MIN(column)`: Returns the smallest value.
- `MAX(column)`: Returns the largest value.

Calculate summary statistics across all orders.
```sql
SELECT 
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS average_amount,
    MIN(total_amount) AS lowest_amount,
    MAX(total_amount) AS highest_amount
FROM orders;
```

## Grouping Data (GROUP BY)

The `GROUP BY` clause groups rows that share identical values in specified columns into summary rows. Any column in your `SELECT` list that is not inside an aggregate function must be included in the `GROUP BY` clause.

Count the number of orders and total revenue for each order status.
```sql
SELECT 
    status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS status_revenue
FROM orders
GROUP BY status;
```

## Filtering Groups (HAVING vs WHERE)

Understanding the distinction between `WHERE` and `HAVING` is essential:
- `WHERE` filters individual rows **before** aggregation occurs.
- `HAVING` filters summary groups **after** aggregation occurs.

> [!NOTE]
> You cannot use aggregate functions inside a `WHERE` clause. Use `HAVING` whenever your filter condition relies on an aggregate like `SUM()`, `COUNT()`, or `AVG()`.

Filter individual completed orders first, group them by customer, and then keep only customers who spent over 100 dollars in total.
```sql
SELECT 
    customer_id,
    SUM(total_amount) AS customer_total
FROM orders
WHERE status = 'Completed'
GROUP BY customer_id
HAVING customer_total > 100.00;
```

## Useful Scalar and Date Functions

Scalar functions operate on individual row values and return a single modified value for each row.

### String & Math Functions
- `CONCAT(str1, str2, ...)`: Combines two or more text strings together.
- `UPPER(str)` / `LOWER(str)`: Converts text to all uppercase or lowercase.
- `ROUND(num, decimals)`: Rounds a number to a specified number of decimal places.

Format customer names and round monetary figures.
```sql
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    UPPER(city) AS city_upper,
    ROUND(total_amount, 1) AS rounded_amount
FROM customers;
```

### Date Functions
- `NOW()`: Returns the current date and time.
- `CURDATE()`: Returns today's date.
- `YEAR(date)` / `MONTH(date)`: Extracts the year or month component.
- `DATEDIFF(date1, date2)`: Returns the number of days between two dates.

Filter orders by year and calculate day differences between events.
```sql
SELECT 
    order_id,
    order_date,
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month
FROM orders
WHERE YEAR(order_date) = 2024;
```

## Relational Table Joins

Relational databases store related information across separate tables. Joins allow you to reconnect these tables in your queries using shared keys.

### 1. INNER JOIN (Matching Rows Only)

An `INNER JOIN` returns only the rows where there is a matching value in both tables. Records that do not find a match are excluded.

Join orders with customers to display order details alongside customer names.
```sql
SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    c.first_name,
    c.last_name
FROM orders o
INNER JOIN customers c 
    ON o.customer_id = c.customer_id;
```

### 2. LEFT JOIN (All Left Rows + Matching Right Rows)

A `LEFT JOIN` returns every row from the left table, regardless of whether a match exists on the right. If there is no match, columns from the right table are filled with `NULL`.

List all customers along with their order IDs, including customers who have never placed an order.
```sql
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id;
```

### 3. RIGHT JOIN (All Right Rows + Matching Left Rows)

A `RIGHT JOIN` returns every row from the right table, plus matching rows from the left table. If there is no match, columns from the left table are filled with `NULL`.

List all orders and match customer details, ensuring all order records are preserved.
```sql
SELECT 
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
RIGHT JOIN orders o 
    ON c.customer_id = o.customer_id;
```

### 4. CROSS JOIN (Cartesian Product)

A `CROSS JOIN` pairs every row from the first table with every single row from the second table without needing a condition. If table A has 5 rows and table B has 4 rows, the result contains 20 rows.

Generate every possible combination of customer cities and order statuses.
```sql
SELECT DISTINCT 
    c.city,
    o.status
FROM customers c
CROSS JOIN orders o;
```

### 5. FULL OUTER JOIN (All Rows from Both Tables)

A `FULL OUTER JOIN` returns all records when there is a match in either left or right table, filling with `NULL` where data is missing. MySQL does not have a native `FULL OUTER JOIN` keyword, so it is emulated by combining a `LEFT JOIN` and a `RIGHT JOIN` using `UNION`.

Emulate a full outer join between customers and orders using UNION.
```sql
SELECT 
    c.customer_id,
    c.first_name,
    o.order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
UNION
SELECT 
    c.customer_id,
    c.first_name,
    o.order_id,
    o.total_amount
FROM customers c
RIGHT JOIN orders o 
    ON c.customer_id = o.customer_id;
```
