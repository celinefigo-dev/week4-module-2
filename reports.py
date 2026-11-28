
from database import connect_database
from datetime import date


# Generate an academic summary for each student
def academic_report():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.first_name,
               students.last_name,
               COUNT(grades.grade_id),
               AVG(grades.score),
               MAX(grades.score),
               MIN(grades.score)
        FROM students
        INNER JOIN grades
        ON students.student_id = grades.student_id
        GROUP BY students.student_id
    """)

    records = cursor.fetchall()

    print("\n--- Student Academic Report ---")

    if not records:
        print("No academic records found.")

    for record in records:
        print(f"\nStudent: {record[0]} {record[1]}")
        print(f"Total subjects: {record[2]}")
        print(f"Average score: {record[3]:.2f}%")
        print(f"Highest score: {record[4]:.2f}%")
        print(f"Lowest score: {record[5]:.2f}%")

    conn.close()


# Retrieve grades within a selected date range
def filter_by_date():
    print("\n--- Filter Grades by Date ---")

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        start = date.fromisoformat(start_date)
        end = date.fromisoformat(end_date)

        if start > end:
            print("Start date cannot be after end date.")
            return

    except ValueError:
        print("Please enter valid dates.")
        return

    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.first_name,
               students.last_name,
               grades.subject,
               grades.score,
               grades.assessment_date
        FROM students
        INNER JOIN grades
        ON students.student_id = grades.student_id
        WHERE grades.assessment_date BETWEEN ? AND ?
        ORDER BY grades.assessment_date
    """, (start.isoformat(), end.isoformat()))

    records = cursor.fetchall()

    if not records:
        print("No records found within this date range.")

    for record in records:
        print(
            f"{record[0]} {record[1]} | "
            f"{record[2]} | "
            f"{record[3]}% | "
            f"{record[4]}"
        )

    conn.close()


# Test the report functions
if __name__ == "__main__":
    academic_report()
    filter_by_date()
