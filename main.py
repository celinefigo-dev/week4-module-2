
from database import create_tables
from students import (
    add_student,
    view_students,
    update_student,
    delete_student
)
from grades import add_grade, view_grades
from reports import academic_report, filter_by_date


# Display the main menu
def display_menu():
    print("\n========================================")
    print("   STUDENT RECORDS MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add new student")
    print("2. View all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Add student grade")
    print("6. View student grades")
    print("7. Generate academic report")
    print("8. Filter grades by date")
    print("0. Exit")
    print("========================================")


# Run the application and process user choices
def main():
    create_tables()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                update_student()

            elif choice == "4":
                delete_student()

            elif choice == "5":
                add_grade()

            elif choice == "6":
                view_grades()

            elif choice == "7":
                academic_report()

            elif choice == "8":
                filter_by_date()

            elif choice == "0":
                print("Thank you for using the system!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter valid information.")


# Start the application
if __name__ == "__main__":
    main()
