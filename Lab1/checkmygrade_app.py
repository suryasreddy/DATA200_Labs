import sys
from managers.csv_manager import CSVManager
from managers.app_manager import AppManager

# Import updated models (with new static methods, etc.)
from models.student import Student
from models.course import Course
from models.professor import Professor
from models.login_user import LoginUser

def main_menu():
    print("\n===== CheckMyGrade Application =====")
    print("1.  Login")
    print("2.  Register New User")
    print("3.  Add Student")
    print("4.  Search Student")
    print("5.  Sort Students by First Name")
    print("6.  Delete Student")
    print("7.  Course Average Marks")
    print("8.  Add Professor")
    print("9.  Delete Professor")
    print("10. Search Professor")
    print("11. Modify Professor")
    print("12. Add Course")
    print("13. Delete Course")
    print("14. Search Course")
    print("15. Change User Password")
    print("16. Logout User")
    print("17. Exit")

def run_app():
    # Initialize CSVManager (reads/writes CSV files)
    csv_manager = CSVManager(base_path="data")
    # Initialize AppManager (manages in-memory LinkedLists + CSV sync)
    app_manager = AppManager(csv_manager)

    while True:
        main_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            # LOGIN
            user_id = input("Enter user ID (email): ")
            password = input("Enter password: ")
            role = app_manager.validate_login(user_id, password)
            if role:
                print(f"Login successful. Role: {role}")
            else:
                print("Invalid credentials.")
        
        elif choice == '2':
            # REGISTER NEW USER
            user_id = input("Enter new user ID (email): ")
            password = input("Enter password: ")
            role = input("Enter role (student/professor/admin): ")
            new_login = LoginUser(user_id, password, role)
            app_manager.add_login_user(new_login)
            print("User registered successfully.")
        
        elif choice == '3':
            # ADD STUDENT
            # Option A: Directly prompt user for data (programmatic approach)
            email = input("Student email: ")
            fname = input("First name: ")
            lname = input("Last name: ")
            course_id = input("Course ID: ")
            grade = input("Grade (A/B/C etc.): ")
            marks = int(input("Marks: "))
            st = Student(email, fname, lname, course_id, grade, marks)
            app_manager.add_student(st)
            print("Student added.")

            # Option B (if you want to use the new static method):
            # app_manager.add_student_interactive()

        elif choice == '4':
            # SEARCH STUDENT
            email = input("Enter student email to search: ")
            student_found = app_manager.search_student(email)
            if student_found:
                print("Student found:", student_found)
            else:
                print("Student not found.")
        
        elif choice == '5':
            # SORT STUDENTS BY FIRST NAME
            app_manager.sort_students_by_name()
            print("Students sorted by first name.")
        
        elif choice == '6':
            # DELETE STUDENT
            email = input("Enter student email to delete: ")
            success = app_manager.delete_student(email)
            if success:
                print("Student deleted.")
            else:
                print("Student not found.")

            # Or, if you want to use the new static method:
            # app_manager.delete_student_interactive()

        elif choice == '7':
            # COURSE AVERAGE MARKS
            cid = input("Enter course ID to compute average: ")
            avg = app_manager.get_course_average(cid)
            print(f"Average marks for course {cid}: {avg:.2f}")

        elif choice == '8':
            # ADD PROFESSOR
            # Interactive approach (prompts user for professor data)
            app_manager.add_professor_interactive()

        elif choice == '9':
            # DELETE PROFESSOR
            # Interactive approach
            app_manager.delete_professor_interactive()

        elif choice == '10':
            # SEARCH PROFESSOR
            prof_id = input("Enter professor ID or email to search: ")
            prof_found = app_manager.search_professor(prof_id)
            if prof_found:
                print("Professor found:", prof_found)
            else:
                print("Professor not found.")

        elif choice == '11':
            # MODIFY PROFESSOR
            prof_id = input("Enter professor ID or email to modify: ")
            print("Enter new details (leave blank to skip):")
            new_name = input("New Name: ").strip()
            new_email = input("New Email: ").strip()
            new_rank = input("New Rank: ").strip()
            new_course = input("New Course ID: ").strip()

            # Build kwargs only for non-empty fields
            kwargs = {}
            if new_name:
                kwargs["name"] = new_name
            if new_email:
                kwargs["email_address"] = new_email
            if new_rank:
                kwargs["rank"] = new_rank
            if new_course:
                kwargs["course_id"] = new_course

            success = app_manager.modify_professor(prof_id, **kwargs)
            if success:
                print("Professor modified successfully.")
            else:
                print("Professor not found.")

        elif choice == '12':
            # ADD COURSE
            app_manager.add_course_interactive()

        elif choice == '13':
            # DELETE COURSE
            app_manager.delete_course_interactive()

        elif choice == '14':
            # SEARCH COURSE
            cid = input("Enter Course ID to search: ")
            course_found = app_manager.search_course(cid)
            if course_found:
                print("Course found:", course_found)
            else:
                print("Course not found.")

        elif choice == '15':
            # CHANGE USER PASSWORD
            uid = input("Enter user ID (email) to change password: ")
            new_pw = input("Enter new password: ")
            success = app_manager.change_user_password(uid, new_pw)
            if success:
                print("Password changed successfully.")
            else:
                print("User not found.")

        elif choice == '16':
            # LOGOUT USER
            uid = input("Enter user ID (email) to logout: ")
            success = app_manager.logout_user(uid)
            if success:
                print("User logged out successfully.")
            else:
                print("User not found or not logged in.")

        elif choice == '17':
            # EXIT
            print("Exiting application.")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_app()


