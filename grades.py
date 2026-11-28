
import sqlite3
from database import connect_database
from students import view_students


# Add a student grade
def add_grade():
    print("\n--- Add Student Grade ---")

    view_students()

    try:
        student_id = int(input("\nEnter student ID: "))
        subject = input("Enter subject: ")
        score = float(input("Enter score (0-100): "))

        if not 0 <= score <= 100:
            print("Score must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    conn = connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO grades
            (student_id, subject, score)
            VALUES (?, ?, ?)
        """, (student_id, subject, score))

        conn.commit()
        print("Grade added successfully!")

    except sqlite3.IntegrityError as error:
        print("Unable to add grade:", error)

    finally:
        conn.close()


# View student grades using SQL JOIN
def view_grades():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.student_id,
               students.first_name,
               students.last_name,
               grades.subject,
               grades.score,
               grades.assessment_date
        FROM students
        INNER JOIN grades
        ON students.student_id = grades.student_id
        ORDER BY students.student_id
    """)

    records = cursor.fetchall()

    print("\n--- Student Academic Records ---")

    if not records:
        print("No grades found.")
    else:
        for record in records:
            print(
                f"ID: {record[0]} | "
                f"Name: {record[1]} {record[2]} | "
                f"Subject: {record[3]} | "
                f"Score: {record[4]:.1f}% | "
                f"Date: {record[5]}"
            )

    conn.close()


# Test the functions
if __name__ == "__main__":
    add_grade()
    view_grades()
