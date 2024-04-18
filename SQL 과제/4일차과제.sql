-- CREATE DATABASE 과제4
-- USE 과제4
-- CREATE TABLE employees (id INT PRIMARY KEY AUTO_INCREMENT,
-- employee_name VARCHAR(100), employee_position VARCHAR(100),
-- salary DECIMAL(10, 2))

-- INSERT INTO employees(employee_name, employee_position, salary)
-- VALUES('혜린', 'PM', 90000),
-- 	('은우', 'Frontend',80000),
--     ('가을', 'Backend', 92000),
--     ('지수', 'Frontend', 78000),
-- 	('민혁', 'Frontend', 96000),
--     ('하온', 'Backend', 130000);


-- SELECT employee_name , employee_position FROM employees

-- SELECT employee_name , salary FROM employees WHERE employee_position='Frontend' AND salary < 90000

-- UPDATE employees SET salary= salary * 1.1 WHERE employee_position='PM'
-- SELECT * FROM employees

-- UPDATE employees SET salary= salary * 1.05 WHERE employee_position='Backend'
-- SELECT * FROM employees

-- DELETE FROM employees WHERE employee_name='민혁'
-- SELECT * FROM employees

-- SELECT AVG(salary), employee_position FROM employees GROUP BY employee_position;

-- DROP TABLE employees
