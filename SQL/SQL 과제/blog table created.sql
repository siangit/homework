-- CREATE Database blog
-- USE blog 
CREATE TABLE posts (
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);