-- Homework Lesson 4: Relational Joins and Database Views
--
-- SETUP SCRIPT: Run this entire block first to create the testing environment.
-- Do not modify the setup code.

CREATE SCHEMA IF NOT EXISTS homework_lesson4;
USE homework_lesson4;

DROP TABLE IF EXISTS employee_projects;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    department_id INT,
    manager_id INT DEFAULT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12,2) NOT NULL
);

CREATE TABLE employee_projects (
    employee_id INT,
    project_id INT,
    hours_allocated INT NOT NULL,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

INSERT INTO departments (dept_name, location) VALUES
('Engineering', 'San Francisco'),
('Marketing', 'New York'),
('Finance', 'Chicago'),
('Human Resources', 'San Francisco'),
('Legal', 'Boston');

INSERT INTO employees (first_name, last_name, salary, hire_date, department_id, manager_id) VALUES
('Linus', 'Torvalds', 140000.00, '2017-05-15', 1, NULL),
('Ada', 'Lovelace', 125000.00, '2019-06-01', 1, 1),
('Grace', 'Hopper', 130000.00, '2018-01-10', 1, 1),
('Alan', 'Turing', 120000.00, '2021-09-20', 1, 2),
('Don', 'Draper', 88000.00, '2022-04-12', 2, NULL),
('Peggy', 'Olson', 92000.00, '2021-11-05', 2, 5),
('Alexander', 'Hamilton', 95000.00, '2020-03-15', 3, NULL),
('Thomas', 'Jefferson', 91000.00, '2023-02-18', 3, 7),
('Toby', 'Flenderson', 65000.00, '2022-08-01', 4, NULL),
('Stanley', 'Hudson', 72000.00, '2023-07-10', 2, 5);

INSERT INTO projects (project_name, budget) VALUES
('Cloud Migration', 250000.00),
('Brand Rebranding', 80000.00),
('Annual Audit', 45000.00),
('AI Assistant Dev', 400000.00),
('Security Compliance', 60000.00);

INSERT INTO employee_projects (employee_id, project_id, hours_allocated) VALUES
(2, 1, 25),
(2, 4, 15),
(3, 1, 20),
(3, 4, 20),
(4, 4, 35),
(1, 1, 40),
(5, 2, 30),
(6, 2, 35),
(7, 3, 25),
(8, 3, 20);

-- ==============================================================================
-- ASSIGNMENT TASKS
-- Write your SQL queries below each TODO comment.
-- Apply the concepts from Lesson 4:
-- Relational Joins (INNER, LEFT, RIGHT, Self Join) and Database Views.
-- ==============================================================================

-- TODO 1: 2-Table INNER JOIN (Department Roster)
-- Join employees and departments on department_id to list each employee's
-- first_name, last_name, dept_name, location, and salary.
-- Order the results by dept_name ascending and salary descending.
-- Expected output: 10 rows showing active employees with their assigned department details.


-- TODO 2: Self JOIN with LEFT JOIN (Management Hierarchy)
-- Join the employees table with itself (aliased as m) on e.manager_id = m.employee_id
-- to display each employee's full name (as employee_name), their salary,
-- and their direct manager's full name (as manager_name).
-- Use a LEFT JOIN and IFNULL() to display 'Top Executive' for employees who have no direct manager.
-- Order by employee_name ascending.
-- Expected output: 10 rows showing all employees and their managers, including 4 top executives.


-- TODO 3: 3-Table Relational Chain (Project Staffing)
-- Connect employees, employee_projects, and projects through foreign keys to list
-- each employee's full name (as employee_name), project_name, and hours_allocated.
-- Order by project_name ascending and hours_allocated descending.
-- Expected output: 10 rows showing all active project assignments.


-- TODO 4: LEFT JOIN Anti-Join (Detecting Unassigned Employees)
-- Perform a LEFT JOIN from employees to employee_projects on employee_id and filter
-- for records where ep.project_id IS NULL to identify employees who are currently
-- not assigned to any project.
-- Display employee_id, first_name, last_name, and hire_date.
-- Expected output: 2 rows (Toby Flenderson, Stanley Hudson).


-- TODO 5: RIGHT JOIN to Identify Unstaffed Projects
-- Perform a RIGHT JOIN from employee_projects to projects on ep.project_id = p.project_id
-- and filter where ep.employee_id IS NULL to identify newly approved projects that have
-- zero assigned team members.
-- Display project_id, project_name, and budget.
-- Expected output: 1 row (Security Compliance).


-- TODO 6: Multi-Table Aggregation with HAVING (Department Workloads)
-- Join departments, employees, and employee_projects to calculate the total allocated
-- project hours across each department (as total_project_hours).
-- Group by dept_name and use a HAVING clause to only display departments with
-- strictly more than 50 total allocated project hours.
-- Order by total_project_hours descending.
-- Expected output: 2 rows (Engineering with 155 hours, Marketing with 65 hours).


-- TODO 7: Creating View — Reusable Staffing Directory (CREATE VIEW)
-- Create or replace a database view named v_staffing_directory that joins
-- employees, departments, employee_projects, and projects using LEFT JOINs.
-- The view must output:
--   - employee_id
--   - full name concatenated as employee_name
--   - dept_name
--   - location
--   - project_name (display 'Unassigned' if project_name IS NULL using IFNULL)
--   - hours_allocated (display 0 if hours_allocated IS NULL using IFNULL)
-- Expected output: View created successfully.


-- TODO 8: Querying & Filtering View
-- Query v_staffing_directory to find all assignments located in 'San Francisco'
-- where the employee is actively assigned to a project (exclude 'Unassigned').
-- Order by hours_allocated descending.
-- Expected output: 6 rows.
