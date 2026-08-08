# Student Management System

A simple **Student Management System** built using **Python** and **MySQL**.
This project is a command-line application that allows users to add, view, search, update, and delete student records stored in a MySQL database.

## Features

The system provides the following operations:

1. **Add Student** – Add a new student to the database.
2. **View Students** – Display all student records.
3. **Search Student** – Search for a student using their student ID.
4. **Update Student** – Update the student's name, age, course, branch, or marks.
5. **Delete Student** – Delete a student record using the student ID.
6. **Exit** – Close the application and database connection.

## Technologies Used

* **Python 3**
* **MySQL**
* **mysql-connector-python**
* **Command Line Interface (CLI)**

## Project Structure

```text
student-management-system/
│
├── student_management.py
└── README.md
```

## Database Setup

First, create the database in MySQL:

```sql
CREATE DATABASE student_management;
```

Select the database:

```sql
USE student_management;
```

Create the `students` table:

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    branch VARCHAR(100),
    marks INT
);
```

## MySQL Connector Installation

Install the MySQL connector using pip:

```bash
pip install mysql-connector-python
```

## Database Configuration

Update the database connection in the Python program according to your MySQL configuration:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_management"
)
```

> **Important:** Do not upload your actual MySQL password to GitHub. Use your own password locally or store it in environment variables.

## How to Run

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go into the project directory:

```bash
cd student-management-system
```

Install the required package:

```bash
pip install mysql-connector-python
```

Run the Python program:

```bash
python student_management.py
```

## Application Menu

When the program starts, the following menu is displayed:

```text
===== STUDENT MANAGEMENT SYSTEM =====

1.Add student
2.View students
3.Search student
4.Update student
5.Delete student
6.Exit

Enter your choice:
```

## Example

### Adding a Student

```text
enter the student id : 101
enter the student name : Vinay
enter the student age : 21
enter the course: Python
enter the branch: Computer Science
enter the student marks: 85

student added successfully to the database
```

### Viewing Students

```text
==== STUDENT DETAILS ====

student_id : 101
name : Vinay
age : 21
course : Python
branch: Computer Science
marks : 85
```

### Searching for a Student

The user can enter a student ID to find a particular student:

```text
enter the student id to search: 101

student found:
student_id : 101
name : Vinay
age : 21
course : Python
branch: Computer Science
marks : 85
```

## CRUD Operations

This project demonstrates the basic **CRUD** operations:

| Operation | SQL Command | Purpose                    |
| --------- | ----------- | -------------------------- |
| Create    | `INSERT`    | Add a student              |
| Read      | `SELECT`    | View/search students       |
| Update    | `UPDATE`    | Modify student information |
| Delete    | `DELETE`    | Remove a student           |

## Learning Objectives

This project helps demonstrate:

* Python programming fundamentals
* Object-oriented programming using classes
* MySQL database connectivity
* SQL `INSERT`, `SELECT`, `UPDATE`, and `DELETE`
* User input handling
* Command-line application development
* Connecting Python applications with databases

## Future Improvements

Possible improvements for this project include:

* Add input validation
* Handle duplicate student IDs
* Add better error handling for database errors
* Use environment variables for database credentials
* Improve the CLI interface
* Add sorting and filtering of students
* Add a graphical user interface (GUI)
* Add login/authentication functionality
* Separate database operations into different functions

## Author

**Vinay**

This project was created as a learning project to practice **Python, MySQL, SQL, and CRUD operations**.
