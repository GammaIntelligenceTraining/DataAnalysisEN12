# Lesson 4 Handout: Advanced Joins and Views

This guide serves as a practical reference for multi-table joins and database views.

## Multi-Table Relational Joins

Relational databases structure data across multiple normalized tables. You can chain multiple JOIN clauses sequentially in a single query.

### 3-Table Join via Junction Table
When querying a Many-to-Many relationship, connect the first table to the junction/bridge table, and then connect the junction table to the final table.

Connect employees to projects through the junction table.
```sql
SELECT 
    e.first_name,
    e.last_name,
    p.project_name,
    ep.hours_allocated
FROM employees e
INNER JOIN employee_projects ep 
    ON e.employee_id = ep.employee_id
INNER JOIN projects p 
    ON ep.project_id = p.project_id;
```

### Detecting Missing Relationships (LEFT JOIN ... IS NULL)
A `LEFT JOIN` combined with a `WHERE ... IS NULL` condition identifies records in the primary table that have no corresponding entries in the related table.

Find employees who have not been assigned to any project.
```sql
SELECT 
    e.employee_id,
    e.first_name,
    e.last_name
FROM employees e
LEFT JOIN employee_projects ep 
    ON e.employee_id = ep.employee_id
WHERE ep.project_id IS NULL;
```

## Database Views

A **View** is a saved SQL query that acts like a virtual table. Views do not duplicate stored data; they execute dynamically whenever queried.

### Why Use Views
- **Simplicity:** Hides complex multi-table joins behind a standard table name.
- **Security:** Grants users access to specific computed columns while hiding underlying sensitive tables.
- **Consistency:** Ensures business metrics and calculations are defined in one centralized definition.

### Creating and Querying a View
Create a view summarizing department headcount and payroll.
```sql
CREATE OR REPLACE VIEW v_department_summary AS
SELECT 
    d.dept_name,
    COUNT(e.employee_id) AS total_staff,
    SUM(e.salary) AS total_payroll
FROM departments d
INNER JOIN employees e 
    ON d.department_id = e.department_id
GROUP BY d.dept_name;
```

Query the view using standard WHERE and ORDER BY clauses.
```sql
SELECT * 
FROM v_department_summary
WHERE total_payroll > 200000.00
ORDER BY total_payroll DESC;
```

Remove a view when it is no longer required.
```sql
DROP VIEW IF EXISTS v_department_summary;
```

## Common SQL Debugging Pitfalls

When building complex relational queries and views, developers frequently encounter several error codes and logical traps.

### Foreign Key Constraint Violations (Error Code 1452)
Relational databases enforce referential integrity. Attempting to insert or update a child record with a foreign key value that does not exist in the parent table triggers MySQL Error 1452.

Attempting to insert an order item referencing non-existent product ID 999.
```sql
-- Fails with Error Code 1452: Cannot add or update a child row (foreign key constraint fails)
INSERT INTO order_items (order_id, product_id, quantity, line_total)
VALUES (1, 999, 1, 50.00);
```

Correcting the insert with an existing parent product ID.
```sql
INSERT INTO order_items (order_id, product_id, quantity, line_total)
VALUES (1, 3, 1, 350.00);
```

### Accidental Cartesian Products (Missing Join Condition)
If a query joins two tables without specifying an `ON` clause, MySQL generates a Cartesian product (`CROSS JOIN`), pairing every row of Table A with every row of Table B.

Accidental Cartesian product multiplying row counts.
```sql
-- Returns 6 customers * 7 orders = 42 rows instead of matching orders
SELECT c.full_name, o.order_id
FROM customers c
JOIN orders o;
```

Corrected inner join using an explicit ON condition.
```sql
-- Returns only the 7 actual placed orders
SELECT c.full_name, o.order_id
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

### Ambiguous Column References (Error Code 1052)
When multiple joined tables contain columns with identical names (such as `customer_id`), referencing that column without prefixing its table or table alias produces MySQL Error 1052.

Unqualified column reference producing ambiguity error.
```sql
-- Fails with Error Code 1052: Column 'customer_id' in field list is ambiguous
SELECT customer_id, full_name, order_id
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

Corrected query qualifying all shared columns with table aliases.
```sql
SELECT c.customer_id, c.full_name, o.order_id
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

### Handling NULL Values in Outer Join Aggregations
When performing a `LEFT JOIN`, primary rows without matching records return `NULL` for right-side columns. Performing mathematical operations or aggregations like `SUM()` on missing values results in `NULL` instead of 0.

Protecting calculations against NULL using the IFNULL function.
```sql
SELECT 
    c.customer_id,
    c.full_name,
    IFNULL(SUM(oi.line_total), 0) AS total_spend
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.full_name;
```

### Filtering Outer Joins in WHERE vs ON Clauses
Placing a filter condition for the optional table in the `WHERE` clause unintentionally eliminates unmatched rows because comparing `NULL` to a value evaluates to `UNKNOWN`/`FALSE`. This converts the `LEFT JOIN` into an `INNER JOIN`.

Moving the filter condition into the join ON clause to preserve unmatched rows.
```sql
SELECT 
    c.customer_id,
    c.full_name,
    COUNT(o.order_id) AS delivered_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'Delivered'
GROUP BY c.customer_id, c.full_name;
```
