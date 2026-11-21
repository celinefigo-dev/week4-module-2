
import sqlite3


# Connect to the database
def connect_database():
    conn = sqlite3.connect("student_records.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# Create database tables
def create_tables():
    conn = connect_database()
    cursor = conn.cursor()

    # Create students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            grade_level INTEGER NOT NULL,
            enrollment_date DATE DEFAULT CURRENT_DATE
        )
    """)

    # Create grades table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            score REAL CHECK(score BETWEEN 0 AND 100),
            assessment_date DATE DEFAULT CURRENT_DATE,
            FOREIGN KEY (student_id)
                REFERENCES students(student_id)
                ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully!")


if __name__ == "__main__":
    create_tables()