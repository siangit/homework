-- USE 이시안;

-- CREATE TABLE DB_basic (
-- 	user_id INT PRIMARY KEY AUTO_INCREMENT,
--     user_name TEXT NOT NULL,
--     email TEXT NOT NULL,
--     age INT);

-- INSERT INTO DB_basic (user_name, email, age) VALUES (
-- 'sian_lee', 'sian@example.com', 28);


-- INSERT INTO DB_basic (user_name, email) VALUES (
-- 'sungwoo', 'sungwoo@example.com');

-- INSERT INTO DB_basic (user_name, email, age) VALUES (
-- 'mijin','',30)

-- INSERT INTO DB_basic (user_name, email, age) 
-- VALUES ('younggwang','younggwang@exmple.com',29),
-- 		('seunghyun','seunghyun@exmaple.com',26),
--         ('jongkyung','jk@example.com', 28);
--         
-- INSERT INTO DB_basic (user_name, email, age) VALUES(
-- 'sian','sian@example.com', 24) 
-- ON DUPLICATE KEY UPDATE age = 28;

-- SELECT user_name FROM DB_basic;
-- SELECT DISTINCT name , age FROM DB_basic;

-- SELECT age, age+1 AS NXTyear FROM DB_basic

-- SELECT * FROM DB_basic ORDER BY age DESC
-- SELECT * FROM DB_basic ORDER BY user_id ASC

-- SELECT * FROM DB_basic WHERE age=28;
-- SELECT * FROM DB_basic WHERE age=28 AND user_name='sian_lee'

-- SELECT * FROM DB_basic LIMIT 2;

-- SELECT * FROM DB_basic LIMIT 3,4;

-- SELECT age, COUNT(*) as DB_count FROM DB_basic GROUP BY age;

-- SELECT user_name, age, 
-- CASE WHEN age>=29 THEN '성인' 
-- ELSE '미성년자' END AS age_group FROM DB_basic;

-- SELECT email, age,
-- CASE WHEN age<30 THEN '20대' ELSE '30대' 
-- END AS age_group FROM DB_basic

-- select 값을 보여줘 from 테이블 join 합칠테이블 on 얘네값이 같다는 것을 참조해서 
-- SELECT DB_basic.user_name,DB_basic.age, orders.order_id 
-- FROM DB_basic JOIN orders ON DB_basic.user_id=orders.user_id

-- SELECT * FROM DB_basic

-- SELECT user_name, age, 
-- ROW_NUMBER() OVER (ORDER BY age DESC) AS ranking FROM DB_basic;

-- UPDATE DB_basic SET user_name='jungkook' WHERE user_id=9;