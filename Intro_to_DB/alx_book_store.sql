-- Database: alx_book_store
-- Online Bookstore Database Schema
-- This database stores information about books, authors, customers, orders, and order details

-- Create the database
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- Authors table: Stores information about authors
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Customers table: Stores information about customers
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE,
    address TEXT
);

-- Books table: Stores information about books available in the bookstore
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
);

-- Orders table: Stores information about orders placed by customers
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Order_Details table: Stores information about the books included in each order
CREATE TABLE Order_Details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_books_author ON Books(author_id);
CREATE INDEX idx_orders_customer ON Orders(customer_id);
CREATE INDEX idx_order_details_order ON Order_Details(order_id);
CREATE INDEX idx_order_details_book ON Order_Details(book_id);
CREATE INDEX idx_customers_email ON Customers(email);

-- Insert sample data for testing
INSERT INTO Authors (author_name) VALUES
('George Orwell'),
('Jane Austen'),
('J.K. Rowling'),
('Harper Lee'),
('F. Scott Fitzgerald');

INSERT INTO Customers (customer_name, email, address) VALUES
('John Smith', 'john.smith@email.com', '123 Main St, New York, NY 10001'),
('Sarah Johnson', 'sarah.j@email.com', '456 Oak Ave, Los Angeles, CA 90210'),
('Mike Brown', 'mike.brown@email.com', '789 Pine St, Chicago, IL 60601');

INSERT INTO Books (title, author_id, price, publication_date) VALUES
('1984', 1, 12.99, '1949-06-08'),
('Pride and Prejudice', 2, 9.99, '1813-01-28'),
('Harry Potter and the Philosopher\'s Stone', 3, 15.99, '1997-06-26'),
('To Kill a Mockingbird', 4, 11.99, '1960-07-11'),
('The Great Gatsby', 5, 10.99, '1925-04-10');

INSERT INTO Orders (customer_id, order_date) VALUES
(1, '2024-01-15'),
(2, '2024-01-16'),
(1, '2024-01-20'),
(3, '2024-01-22');

INSERT INTO Order_Details (order_id, book_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(3, 4, 1),
(3, 5, 1),
(4, 1, 1),
(4, 3, 2);
