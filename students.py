
import sqlite3
from database import connect_database


# Add a new student
def add_student():
    print("\n--- Add New Student ---")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    grade_level = int(input("Enter grade level: "))

    conn = connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO students
            (first_name, last_name, email, grade_level)
            VALUES (?, ?, ?, ?)
        """, (first_name, last_name, email, grade_level))

        conn.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError as error:
        print("Unable to add student:", error)

    finally:
        conn.close()


# View all students
def view_students():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n--- Student Records ---")

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} {student[2]} | "
                f"Email: {student[3]} | "
                f"Grade: {student[4]} | "
                f"Enrolled: {student[5]}"
            )

    conn.close()


# Update student information
def update_student():
    view_students()

    student_id = int(input("\nEnter student ID to update: "))
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    email = input("Enter new email: ")
    grade_level = int(input("Enter new grade level: "))

    conn = connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE students
            SET first_name = ?, last_name = ?,
                email = ?, grade_level = ?
            WHERE student_id = ?
        """, (first_name, last_name, email,
              grade_level, student_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    except sqlite3.IntegrityError as error:
        print("Unable to update student:", error)

    finally:
        conn.close()


# Delete a student
def delete_student():
    view_students()

    student_id = int(input("\nEnter student ID to delete: "))

    confirm = input(
        "Delete this student and their grades? (yes/no): "
    )

    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return

    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM students
        WHERE student_id = ?
    """, (student_id,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

    conn.close()


# Test the functions
if __name__ == "__main__":
    add_student()
    view_students()
