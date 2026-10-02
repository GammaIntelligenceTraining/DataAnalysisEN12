# Lesson 2 Handout: Basic SQL Querying

This guide serves as a quick reference for the SQL commands covered in Lesson 2. 

## Reading Data (SELECT)

The SELECT statement is used to retrieve data from a database. You can select all columns using an asterisk (*), or specify exact columns for better performance.

Select specific columns from the actor table.
```sql
SELECT first_name, last_name FROM actor;
```

To remove duplicate entries from your results, use the DISTINCT keyword.

Select only unique first names.
```sql
SELECT DISTINCT first_name FROM actor;
```

## Sorting and Limiting Output

You can control the order of your results using ORDER BY (ASC for ascending, DESC for descending) and restrict the total number of rows returned using LIMIT.

Sort actors by last name alphabetically, and only show the first 10 results.
```sql
SELECT first_name, last_name 
FROM actor 
ORDER BY last_name ASC 
LIMIT 10;
```

## Filtering Data (WHERE)

The WHERE clause filters rows based on a specific condition, returning only the rows where the condition is true.

Find all films where the rental duration is greater than 5 days.
```sql
SELECT * FROM film WHERE rental_duration > 5;
```

## Logical Operators (AND, OR, NOT)

You can chain multiple conditions together.

Find all films that are rated either PG or G.
```sql
SELECT * FROM film WHERE rating = 'PG' OR rating = 'G';
```

## Pattern Matching (LIKE)

Use the LIKE operator to find strings matching a specific pattern. 
- The `%` symbol represents zero, one, or multiple characters.
- The `_` symbol represents exactly one character.

Find all actors whose first name starts with the letter 'A'.
```sql
SELECT * FROM actor WHERE first_name LIKE 'A%';
```

## Lists and Ranges (IN, BETWEEN)

The IN operator replaces long chains of OR conditions. The BETWEEN operator is used to filter within a numerical or date range.

Find all films that have a runtime between 90 and 120 minutes.
```sql
SELECT * FROM film WHERE length BETWEEN 90 AND 120;
```

Find actors whose first name is Nick, Ed, or Johnny.
```sql
SELECT * FROM actor WHERE first_name IN ('NICK', 'ED', 'JOHNNY');
```

## Checking for Empty Data (IS NULL)

In a database, missing data is represented by NULL. You cannot use the equals sign to check for NULL.

Find all addresses where the second address line is empty.
```sql
SELECT * FROM address WHERE address2 IS NULL;
```

## Modifying Data (DML)

Data Manipulation Language allows you to write and alter data. 

> [!WARNING]
> Always use a WHERE clause when updating or deleting data. If you omit the WHERE clause, your change will apply to every single row in the table!

Insert a brand new record into the actor table.
```sql
INSERT INTO actor (first_name, last_name) VALUES ('JOHN', 'DOE');
```

Update an existing record's first name.
```sql
UPDATE actor SET first_name = 'JACK' WHERE last_name = 'DOE';
```

Delete a specific record entirely.
```sql
DELETE FROM actor WHERE first_name = 'JACK';
```
