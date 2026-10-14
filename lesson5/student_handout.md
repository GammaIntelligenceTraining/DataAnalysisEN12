# Lesson 5 Handout: Window Functions and Foreign Key Architecture

This guide provides technical explanations, syntax reference patterns, and real-world examples for advanced analytical Window Functions and relational Foreign Key constraints in MySQL.

---

## Part 1: Advanced Analytics and Window Functions

A **Window Function** performs calculations across a set of table rows that are related to the current row. Unlike standard `GROUP BY` aggregations, window functions **do not collapse rows**; each row retains its unique identity while displaying computed aggregate metrics alongside it.

### Core Syntax Structure

```sql
<function_name>(<expression>) OVER (
    [PARTITION BY <column_1>, <column_2>]
    [ORDER BY <sort_column> [ASC|DESC]]
)
```

- **`OVER ()`:** Signals to MySQL that the function is a window function. If left empty, the window covers the entire result set.
- **`PARTITION BY`:** Divides the rows into analytical partitions (groups). The calculation resets when crossing partition boundaries.
- **`ORDER BY`:** Sorts the rows inside each partition. Essential for rankings, running totals, and offset functions.

---

### Non-Collapsing Aggregates (`OVER` vs. `GROUP BY`)

Standard aggregate functions (`AVG`, `SUM`, `COUNT`, `MIN`, `MAX`) can be used as window functions simply by appending the `OVER()` clause.

Compare each film duration to the global average across all films in Sakila.
```sql
SELECT 
    film_id,
    title,
    length,
    ROUND(AVG(length) OVER (), 1) AS overall_avg_length,
    length - ROUND(AVG(length) OVER (), 1) AS diff_from_avg
FROM film
ORDER BY length DESC
LIMIT 10;
```

---

### Partitioning Data (`PARTITION BY`)

Using `PARTITION BY` recalculates metrics for each logical group without hiding individual row details.

Compute the average film length per rating category and compare individual films against their rating benchmark.
```sql
SELECT 
    title,
    rating,
    length,
    ROUND(AVG(length) OVER (PARTITION BY rating), 1) AS rating_avg_length,
    length - ROUND(AVG(length) OVER (PARTITION BY rating), 1) AS diff_from_rating_avg
FROM film
ORDER BY rating, length DESC;
```

---

### Ranking Functions Suite

MySQL provides three primary ranking functions. Their differences lie entirely in how they resolve tied values:

| Function | Tie Handling | Rank Sequence Example |
| :--- | :--- | :--- |
| **`ROW_NUMBER()`** | No ties allowed. Assigns arbitrary consecutive integers. | 1, 2, 3, 4, 5 |
| **`RANK()`** | Allows ties. Skips subsequent rank numbers after ties. | 1, 2, 2, 4, 5 |
| **`DENSE_RANK()`** | Allows ties. Does not skip rank numbers. | 1, 2, 2, 3, 4 |

Compare ranking behavior on tied film lengths.
```sql
SELECT 
    title,
    rating,
    length,
    ROW_NUMBER() OVER (PARTITION BY rating ORDER BY length DESC) AS row_num,
    RANK() OVER (PARTITION BY rating ORDER BY length DESC) AS rnk,
    DENSE_RANK() OVER (PARTITION BY rating ORDER BY length DESC) AS dense_rnk
FROM film
WHERE rating = 'G'
ORDER BY length DESC
LIMIT 10;
```

### Filtering Top-N Records Using Subqueries

Because SQL processes the `WHERE` clause before evaluating `SELECT` expressions, window function aliases cannot be referenced directly in `WHERE`. You must wrap the query in a subquery or Common Table Expression (CTE).

Filter for the Top 2 longest films within each rating category.
```sql
SELECT *
FROM (
    SELECT 
        title,
        rating,
        length,
        DENSE_RANK() OVER (PARTITION BY rating ORDER BY length DESC) AS length_rank
    FROM film
) AS ranked_films
WHERE length_rank <= 2
ORDER BY rating, length_rank;
```

---

### Cumulative Metrics (Running Totals)

When an aggregate function like `SUM()` is combined with an `ORDER BY` clause inside `OVER()`, MySQL evaluates an **expanding window frame** from the start of the partition up to the current row.

Calculate a cumulative running total of payments made by a customer over time.
```sql
SELECT 
    payment_id,
    customer_id,
    payment_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date
    ) AS running_spend
FROM payment
WHERE customer_id = 1
ORDER BY payment_date;
```

---

### Value Navigation (`LAG` and `LEAD`)

Navigation functions access values from adjacent rows without performing expensive self-joins:
- **`LAG(column, offset, default_value)`:** Reads from a preceding row.
- **`LEAD(column, offset, default_value)`:** Reads from a subsequent row.

Calculate the dollar change between each payment and the customer's previous payment.
```sql
SELECT 
    payment_id,
    customer_id,
    payment_date,
    amount AS current_amount,
    LAG(amount, 1, 0.00) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date
    ) AS previous_amount,
    amount - LAG(amount, 1, amount) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date
    ) AS amount_difference
FROM payment
WHERE customer_id = 2
ORDER BY payment_date;
```

---

## Part 2: Foreign Key Architecture and Referential Integrity

A **Foreign Key** is a column (or set of columns) in a child table that references the **Primary Key** of a parent table. It establishes a contract enforced by the database engine to guarantee **Referential Integrity**—ensuring that child rows cannot point to non-existent parent records.

### Core DDL Syntax

Create a parent table and a child table linked by a foreign key constraint.
```sql
-- Parent Table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE
);

-- Child Table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    CONSTRAINT fk_employees_departments 
        FOREIGN KEY (department_id) 
        REFERENCES departments(department_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
```

### Relational Lifecycle Rules

1. **Table Creation:** The parent table must be created before the child table.
2. **Data Ingestion:** Parent records must be inserted before child records referencing them.
3. **Data Deletion:** Child records must be deleted before their parent record, unless a cascading action is configured.
4. **Table Dropping:** The child table must be dropped before the parent table.

---

### Referential Integrity Violations (Error 1452)

Attempting to insert or update a child record with a foreign key that does not exist in the parent table produces **MySQL Error Code 1452**.

Attempting to insert an employee into non-existent department 999.
```sql
-- Fails with Error Code 1452 (foreign key constraint fails)
INSERT INTO employees (full_name, department_id) 
VALUES ('John Doe', 999);
```

---

### Parent Deletion Behaviors (Error 1451 vs. CASCADE)

When attempting to delete a parent record that still has associated child rows:

#### 1. RESTRICT / NO ACTION (Default)
Prevents parent deletion as long as child rows reference it, raising **MySQL Error Code 1451**.

```sql
-- Fails with Error Code 1451 if employees belong to department 1
DELETE FROM departments WHERE department_id = 1;
```

#### 2. ON DELETE CASCADE
Automatically removes all child rows when the parent row is deleted.

Reconfigure constraint to cascade deletions to child rows.
```sql
ALTER TABLE employees DROP FOREIGN KEY fk_employees_departments;

ALTER TABLE employees 
ADD CONSTRAINT fk_employees_departments 
    FOREIGN KEY (department_id) 
    REFERENCES departments(department_id)
    ON DELETE CASCADE;

-- Deleting department 1 now automatically deletes all associated employees
DELETE FROM departments WHERE department_id = 1;
```

#### 3. ON DELETE SET NULL
Sets the foreign key column in the child table to `NULL` when the parent row is deleted. The foreign key column in the child table must allow `NULL` values.

---

### Teardown Dependencies (Error 3730)

Attempting to drop a parent table while a child table still references it fails with **MySQL Error Code 3730**.

Drop tables in reverse dependency order.
```sql
-- Step 1: Drop child table first
DROP TABLE IF EXISTS employees;

-- Step 2: Drop parent table second
DROP TABLE IF EXISTS departments;
```
