
# Overview

As a software developer, I wanted to improve my knowledge
of SQL relational databases and Python programming.

I developed a Student Records Management System using
Python and SQLite. The software allows users to add,
view, update, and delete student records. Users can also
add student grades, generate academic reports, and
filter grades within a selected date range.

To use the program, run python main.py and select an
option from the main menu.

My purpose for writing this software was to learn how
Python interacts with relational databases and how SQL
commands are used to manage and retrieve information.

[Software Demo Video](INSERT_VIDEO_LINK_HERE)

# Relational Database

I used SQLite as my relational database. SQLite allows
me to store and manage information using SQL commands.

My database contains two tables:

## Students Table

- student_id (Primary Key)
- first_name
- last_name
- email
- grade_level
- enrollment_date

## Grades Table

- grade_id (Primary Key)
- student_id (Foreign Key)
- subject
- score
- assessment_date

The two tables are connected using student_id.

I used INSERT, SELECT, UPDATE, and DELETE to manage
student records. I also used INNER JOIN to combine
the two tables.

The aggregate functions COUNT, AVG, MAX, and MIN
are used to generate academic reports. I used BETWEEN
to filter grades within a selected date range.

# Development Environment

- Visual Studio Code
- Python
- SQLite
- Python sqlite3 library
- Python datetime module
- Git and GitHub

# Useful Websites

- [Python SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Official Website](https://www.sqlite.org/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [Python Documentation](https://docs.python.org/3/)

# Future Work

- Create a graphical user interface.
- Add a login system for teachers and administrators.
- Allow users to export academic reports to PDF.
- Add a student attendance tracking feature.
- Improve input validation and error handling.
