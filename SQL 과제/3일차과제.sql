-- CREATE DATABASE 과제
-- USE 과제
-- customers 테이블에 새 고객을 추가하세요. 
-- CREATE TABLE customers (customer_id INT PRIMARY KEY AUTO_INCREMENT);

-- products 테이블에 새 제품을 추가하세요. 
-- CREATE TABLE products (products_id INT PRIMARY KEY AUTO_INCREMENT);

-- employees 테이블에 새 직원을 추가하세요. 
-- CREATE TABLE employees (employees_id INT PRIMARY KEY AUTO_INCREMENT);
-- ALTER TABLE employees ADD employee_name TEXT NOT NULL
-- ALTER TABLE employees ADD employee_position TEXT NOT NULL

-- offices 테이블에 새 사무실을 추가하세요. 
-- CREATE TABLE offices (offices_id INT PRIMARY KEY AUTO_INCREMENT);

-- orders 테이블에 새 주문을 추가하세요.
-- CREATE TABLE orders (orders_id INT PRIMARY KEY AUTO_INCREMENT);

-- orderdetails 테이블에 주문 상세 정보를 추가하세요
-- CREATE TABLE orderdetails (orderdetails_id INT PRIMARY KEY AUTO_INCREMENT);

-- payments 테이블에 지불 정보를 추가하세요.
-- CREATE TABLE payments (payments_id INT PRIMARY KEY AUTO_INCREMENT);

-- productlines 테이블에 제품 라인을 추가하세요.
-- CREATE TABLE productlines (productlines_id INT PRIMARY KEY AUTO_INCREMENT);

-- customers 테이블에 다른 지역의 고객을 추가하세요.
-- ALTER TABLE customers
-- ADD customer_name TEXT NOT NULL
-- ALTER TABLE customers
-- ADD customer_area TEXT NOT NULL
-- INSERT INTO customers (customer_name, customer_area)
	-- VALUES ('SIAN', 'ALABAMA')
-- SELECT * FROM customers

-- products 테이블에 다른 카테고리의 제품을 추가하세요.
-- ALTER TABLE products
-- ADD category TEXT NOT NULL
-- INSERT INTO products (category)
	-- VALUES('cosmetic')


-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
-- SELECT * FROM customers

-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
-- SELECT * FROM products

-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
-- SELECT employee_name, employee_position FROM employees

-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
-- ALTER TABLE offices ADD office_area TEXT NOT NULL
-- SELECT office_area FROM offices

-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
-- SELECT * FROM orders ORDER BY orders_id DESC LIMIT 10

-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
-- SELECT * FROM orderdetails

-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
-- SELECT * FROM payments WHERE payments_id=1

-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
-- ALTER TABLE productlines ADD product_inform TEXT NOT NULL
-- SELECT product_inform FROM productlines

-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
-- SELECT customer_name, customer_area FROM customers WHERE customer_name='sian'

-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
-- ALTER TABLE products ADD price TEXT NOT NULL
-- SELECT price FROM products WHERE price >=30

-- SELECT * FROM customers JOIN employees ON customers.customer_id=employees.employees_id
-- JOIN offices ON customers.customer_id=offices.offices_id
-- JOIN orderdetails ON customers.customer_id=orderdetails.orderdetails_id
-- JOIN orders ON customers.customer_id=orders.orders_id
-- JOIN payments ON customers.customer_id=payments.payments_id
-- JOIN productlines ON customers.customer_id=productlines.productlines_id
-- JOIN products ON customers.customer_id=products.products_id


-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
-- ALTER TABLE customers ADD customer_address TEXT NOT NULL
-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE customers SET customer_area='Tuscaloosa' WHERE customer_name='sian'
-- SELECT * FROM customers

-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
-- UPDATE products SET price='50' WHERE category='cosmetic'
-- SELECT * FROM products

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
-- INSERT INTO employees (employees_id, employee_name, employee_position) VALUES (1, 'sian', 'manager')
-- UPDATE employees SET employee_position='CHAIRMAN' WHERE employee_name='sian'
-- SELECT * FROM employees

-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
-- ALTER TABLE offices ADD office_number INT
-- INSERT INTO offices (offices_id,office_area,office_number) VALUES (1, 'seoul', '334-531-3504')
-- SELECT * FROM offices

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
-- ALTER TABLE orders ADD order_status TEXT NOT NULL
-- INSERT INTO orders (orders_id , order_status) VALUES (1, 'confirmed')
-- UPDATE orders SET order_status='ready' WHERE orders_id=1
-- SELECT * FROM orders

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
-- ALTER TABLE orderdetails ADD QTY INT NOT NULL
-- INSERT INTO orderdetails (orderdetails_id , QTY) VALUES (1, 12)
-- UPDATE orderdetails SET QTY=6 WHERE orderdetails_id=1
-- SELECT * FROM orderdetails

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
-- ALTER TABLE payments ADD payment_method TEXT NOT NULL
-- ALTER TABLE payments ADD price INT NOT NULL
-- INSERT INTO payments (payments_id ,payment_method, price) VALUES (1,'cash', 30000)
-- UPDATE payments SET price=50000 WHERE payments_id=1
-- SELECT * FROM payments


-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
-- INSERT INTO productlines (productlines_id ,product_inform) VALUES (1,'recycle')
-- UPDATE productlines SET product_inform='edible' WHERE productlines_id=1
-- SELECT * FROM productlines

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
-- ALTER TABLE customers ADD email TEXT NOT NULL
-- UPDATE customers SET email='sian@example.com' WHERE customer_name='SIAN'
-- SELECT * FROM customers

-- (10) **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
-- UPDATE products SET price=50000 LIMIT 5
-- SELECT * FROM products


-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
-- DELETE FROM customers WHERE customer_name = 'SIAN'
-- SELECT * FROM customers

-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
-- DELETE FROM products WHERE category = 'cosmetic'
-- SELECT * FROM products


-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
-- DELETE FROM employees WHERE employee_position='CHAIRMAN'
-- SELECT * FROM employees

-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
-- DELETE FROM offices WHERE office_area='seoul'
-- SELECT * FROM offices

-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
-- DELETE FROM orders WHERE order_status='ready'
-- SELECT * FROM orders

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
-- DELETE FROM orderdetails WHERE QTY=6
-- SELECT * FROM orderdetails

-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
-- DELETE FROM payments WHERE payment_method='cash'
-- SELECT * FROM payments

-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
-- DELETE FROM productlines WHERE productlines_id=1
-- SELECT * FROM productlines


-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
-- DELETE FROM customers WHERE customer_area='seoul'
-- SELECT * FROM customers

-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요
-- DELETE FROM products WHERE category='cosmetic'
-- SELECT * FROM products
