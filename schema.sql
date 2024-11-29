
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    class VARCHAR(50) NOT NULL,
    grade VARCHAR(10) NOT NULL
);

INSERT INTO students (name, class, grade) VALUES
('John Doe', '10A', 'A'),
('Jane Smith', '10B', 'B'),
('Alice Johnson', '10C', 'A+');
