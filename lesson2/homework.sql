-- Homework Lesson 2: Basic Querying and Filtering
-- 
-- SETUP SCRIPT: Run this entire block first to create the testing environment.
-- Do not modify the setup code.
-- COPY AND PASTE TO MYSQL WORKBENCH
-- RUN THIS CODE ONCE TO CREATE SAMPLE SCHEMA AND TABLE
-- DELETE CODE AFTER

-- COPY FROM HERE

CREATE SCHEMA IF NOT EXISTS homework_lesson2;
USE homework_lesson2;

DROP TABLE IF EXISTS video_games;

CREATE TABLE video_games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    release_year INT NOT NULL,
    price DECIMAL(5,2) NOT NULL,
    multiplayer BOOLEAN NOT NULL,
    publisher VARCHAR(100)
);

INSERT INTO video_games (title, genre, release_year, price, multiplayer, publisher) VALUES 
('Cosmic Explorers', 'RPG', 2021, 59.99, 1, 'Nova Studios'),
('Speed Racers 4', 'Racing', 2019, 29.99, 1, 'Velocity Games'),
('Mystery Manor', 'Puzzle', 2015, 14.99, 0, 'Enigma Inc'),
('Space Defender', 'Shooter', 2020, 19.99, 1, 'Nova Studios'),
('The Last Hero', 'RPG', 2023, 69.99, 0, 'Epic Tales'),
('Farming Daily', 'Simulation', 2018, 39.99, 1, 'AgriSoft'),
('Zombie Survival', 'Action', 2022, 49.99, 1, 'Undead Corp'),
('City Builder 2000', 'Simulation', 2000, 9.99, 0, 'Retro Gaming'),
('Mystic Quest', 'RPG', 2012, 19.99, 0, 'Epic Tales'),
('Neon Riders', 'Racing', 2023, 59.99, 1, 'Velocity Games'),
('Ghost Hunter', 'Action', 2020, 45.00, 1, 'Undead Corp'),
('Desert Strike', 'Shooter', 2017, 24.99, 1, NULL),
('Alien Invaders', 'Shooter', 1998, 4.99, 0, 'Retro Gaming');

-- COPY END

-- ==============================================================================
-- ASSIGNMENT TASKS
-- Write your SQL queries below each TODO comment.
-- Only use the SELECT statement and clauses covered in Lesson 2.
-- Do not use any built-in functions.
-- ==============================================================================

-- TODO 1: Retrieve all columns and all rows from the video_games table.
-- Expected output: 13 rows showing all game details.


-- TODO 2: Retrieve only the title and price of all games, ordered by price from highest to lowest.
-- Expected output: 13 rows, 2 columns. Highest price (69.99) at the top.


-- TODO 3: Find all games in the 'RPG' genre.
-- Expected output: 3 rows (Cosmic Explorers, The Last Hero, Mystic Quest).


-- TODO 4: Find all games released in the year 2020 or later.
-- Expected output: 6 rows.


-- TODO 5: Find all 'Racing' or 'Simulation' games. Use the IN operator.
-- Expected output: 4 rows.


-- TODO 6: Find all games priced between 15.00 and 40.00. Use the BETWEEN operator.
-- Expected output: 4 rows.


-- TODO 7: Find all games whose title starts with the letter 'M'. Use pattern matching.
-- Expected output: 2 rows (Mystery Manor, Mystic Quest).


-- TODO 8: Find all games published by 'Nova Studios' that are also multiplayer (multiplayer = 1).
-- Expected output: 2 rows.


-- TODO 9: Find all games that do not have a publisher listed (the publisher is NULL).
-- Expected output: 1 row (Desert Strike).


-- TODO 10: Find the top 3 cheapest games in the database.
-- Expected output: 3 rows, starting with Alien Invaders (4.99).
