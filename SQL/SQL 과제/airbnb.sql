-- USE 과제4

-- CREATE TABLE Products (
--     productID INT AUTO_INCREMENT PRIMARY KEY,
--     productName VARCHAR(255) NOT NULL,
--     price DECIMAL(10, 2) NOT NULL,
--     stockQuantity INT NOT NULL,
--     createDate TIMESTAMP);
    
-- CREATE TABLE Customers (
--     customerID INT AUTO_INCREMENT PRIMARY KEY,
--     customerName VARCHAR(255) NOT NULL,
--     email VARCHAR(255) UNIQUE NOT NULL,
--     address TEXT NOT NULL,
--     createDate TIMESTAMP
-- );

-- CREATE TABLE Orders (
--     orderID INT AUTO_INCREMENT PRIMARY KEY,
--     customerID INT,
--     orderDate TIMESTAMP,
--     totalAmount DECIMAL(10, 2),
--     FOREIGN KEY (customerID) REFERENCES Customers(customerID)
-- );