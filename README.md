# attendance-system
Student attendance management system built with Python and MySQL

# 📋 Attendance System

A command-line student attendance management system built with Python and MySQL.

## Features
- Add students with name and roll number
- Mark attendance as Present or Absent
- View all attendance records
- Generate attendance report per student
- Data stored permanently in MySQL database

## Tech Stack
- Python 3
- MySQL
- mysql-connector-python

## Database Setup
Run these commands in MySQL:
```sql
CREATE DATABASE attendance_db;
USE attendance_db;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(20)
);
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    status VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

## How to Run
1. Install dependency:
   pip3 install mysql-connector-python
2. Setup database (see above)
3. Run:
   python3 attendance.py

## Author
Deepak Singh | BCA Student | Chandigarh
