-- I learn sql today

SELECT * FROM sakila.actor;

SELECT * FROM sakila.film;

SELECT last_name, first_name, first_name, first_name FROM sakila.actor;

SELECT *
FROM sakila.actor
ORDER BY first_name DESC, last_name ASC;

SELECT DISTINCT first_name, last_name
FROM sakila.actor
ORDER BY first_name;

SELECT * FROM sakila.film;

SELECT * FROM sakila.film
ORDER BY length DESC LIMIT 10;

-- = - equals
-- <> - not equals
-- < - less than
-- > - greater than
-- <= - less equals
-- >= - greater equals
SELECT * FROM sakila.film
WHERE length <= 60;

SELECT * FROM sakila.actor
WHERE first_name > 'ELL';


SELECT * FROM sakila.film
WHERE length < 60 AND rating = 'PG';

SELECT * FROM sakila.film
WHERE rating = 'PG' OR rating = 'NC-17';

SELECT * FROM sakila.film
WHERE rating = 'PG' OR rating = 'NC-17' AND length < 60;

SELECT * FROM sakila.film
WHERE NOT rating = 'PG';

SELECT * FROM sakila.film
WHERE rating <> 'PG';

SELECT * FROM sakila.actor
WHERE first_name LIKE "E___%";

SELECT * FROM sakila.actor
WHERE first_name IN ('ED', 'ELVIS', 'EMILY');

SELECT * FROM sakila.film
WHERE length BETWEEN 60 AND 80;

SELECT * FROM sakila.film
WHERE length >= 60 AND length <= 80
ORDER BY length DESC;

SELECT * FROM sakila.actor;

INSERT INTO sakila.actor (first_name, last_name)
VALUES ('BOB', 'DYLAN');

SELECT * FROM sakila.actor
WHERE first_name = 'BOB' AND last_name = 'DYLAN';

SET SQL_SAFE_UPDATES = 1;

UPDATE sakila.actor
SET first_name = 'SIMON'
WHERE actor_id = 230;

SELECT * FROM sakila.actor
WHERE actor_id = 230;

DELETE FROM sakila.actor
WHERE actor_id = 230;

SELECT COUNT(*) FROM sakila.actor;

SELECT COUNT(description) FROM sakila.film;

SELECT COUNT(first_name), SUM(actor_id), AVG(actor_id), MAX(first_name), MIN(first_name)
FROM sakila.actor;

SELECT COUNT(distinct first_name) AS total_unique_names, COUNT(first_name) AS total_names FROM sakila.actor;

USE sakila;

SELECT * FROM actor;

SELECT COUNT(*) AS total_films, AVG(length) AS average_length, rating
FROM film
GROUP BY rating
ORDER BY average_length DESC
LIMIT 2;

SELECT COUNT(*) AS total_films, SUM(replacement_cost) AS total_replacement_cost, rating
FROM film
WHERE length < 100
GROUP BY rating
HAVING total_films > 75;

SELECT SIN(DEGREES(90));

SELECT CEIL(1.5), FLOOR(1.5);

SELECT POWER(10, 2);

SELECT POWER(length, 2) FROM film;

SELECT SQRT(144), POWER(144, 0.5);

SELECT COUNT(first_name) AS total_names,
	COUNT(DISTINCT first_name) AS total_unique_names,
    COUNT(first_name) / COUNT(DISTINCT first_name) AS ratio
FROM actor;

SELECT FORMAT(45.23553465234234, 0);

SELECT REPLACE(first_name, 'ENN', '');

SELECT CONCAT(
			SUBSTRING(first_name, 1, 1),
            LOWER(SUBSTRING(first_name, 2)),
            " ",
			SUBSTRING(last_name, 1, 1),
            LOWER(SUBSTRING(last_name, 2))
		) AS full_name
FROM actor;

SELECT NOW(), CURDATE();

SELECT payment_id, payment_date, DATE(payment_date), YEAR(payment_date), MONTH(payment_date), DAY(payment_date)
FROM payment;

SELECT rental_id, rental_date, return_date, DATEDIFF(return_date, rental_date) AS total_kept
FROM rental;

SELECT payment_id, DATE_FORMAT(payment_date, '%D of %M %Y'), payment_date
FROM payment;

SELECT UNIX_TIMESTAMP();

SELECT actor.first_name, actor.last_name, film.title
FROM actor
RIGHT JOIN film_actor ON actor.actor_id = film_actor.actor_id
RIGHT JOIN film ON film.film_id = film_actor.film_id;


SELECT a.first_name, a.last_name, f.title
FROM actor AS a
RIGHT JOIN film_actor AS fa ON a.actor_id = fa.actor_id
RIGHT JOIN film AS f ON f.film_id = fa.film_id;

SELECT actor.first_name, actor.last_name, film.title
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON actor.actor_id = film_actor.actor_id;

SELECT rating FROM film
UNION ALL
SELECT first_name FROM actor;

SELECT actor.first_name, actor.last_name, film.title
FROM actor
RIGHT JOIN film_actor ON actor.actor_id = film_actor.actor_id
RIGHT JOIN film ON film.film_id = film_actor.film_id
UNION
SELECT actor.first_name, actor.last_name, film.title
FROM actor
LEFT JOIN film_actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film ON film.film_id = film_actor.film_id;

SELECT film.rating, category.name
FROM film
CROSS JOIN category;

show databases;
show tables;
show columns FROM film_actor;

USE sakila;

SELECT
	ci.city_id,
    ci.city,
    co.country
FROM city AS ci
INNER JOIN country AS co
	ON ci.country_id = co.country_id
ORDER BY co.country ASC, ci.city ASC;

SELECT
	c.customer_id,
    c.first_name,
    c.last_name,
    a.address,
    a.district,
    ci.city,
    co.country
FROM customer AS c
INNER JOIN address AS a
	ON c.address_id = a.address_id
INNER JOIN city AS ci
	ON a.city_id = ci.city_id
INNER JOIN country AS co
	ON ci.country_id = co.country_id;
    
SELECT
	f.title AS film_title,
    f.release_year,
    CONCAT(a.first_name, " ", a.last_name) AS full_name
FROM film AS f
INNER JOIN film_actor AS fa
	ON f.film_id = fa.film_id
INNER JOIN actor AS a
	ON fa.actor_id = a.actor_id
WHERE f.title LIKE "ACADEMY%";

SELECT
	f.film_id,
    f.title,
    i.inventory_id
FROM film AS f
LEFT JOIN inventory AS i
	ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

SELECT
	c.customer_id,
    CONCAT(c.first_name, " ", c.last_name) AS full_name,
    COUNT(r.rental_id) AS total_rentals,
    SUM(p.amount) AS total_revenue_spent
FROM customer AS c
INNER JOIN rental AS r
	ON c.customer_id = r.customer_id
INNER JOIN payment AS p
	ON r.rental_id = p.rental_id
-- WHERE MONTH(r.rental_date) in (MONTH(NOW()), MONTH(NOW()) - 1, MONTH(NOW()) - 2)
WHERE YEAR(r.rental_date) = YEAR(NOW())
GROUP BY c.customer_id
ORDER BY total_revenue_spent DESC;


SELECT COUNT(*), rating, rental_duration FROM film
GROUP BY rating, rental_duration;

SELECT
	cat.name AS genre,
    COUNT(DISTINCT f.film_id) AS unique_titles_count,
    COUNT(r.rental_id) AS total_rentals_count,
    SUM(p.amount) AS total_revenue,
    ROUND(AVG(p.amount), 2) AS avg_revenue_per_rental,
    COUNT(r.rental_id) / COUNT(DISTINCT f.film_id) AS relation_between_rentals_and_unique_titles
FROM category AS cat
INNER JOIN film_category AS fc
	ON cat.category_id = fc.category_id
INNER JOIN film AS f
	ON fc.film_id = f.film_id
INNER JOIN inventory AS i
	ON f.film_id = i.film_id
INNER JOIN rental AS r
	ON i.inventory_id = r.inventory_id
INNER JOIN payment AS p
	ON r.rental_id = p.rental_id
GROUP BY cat.name
ORDER BY total_revenue DESC;

