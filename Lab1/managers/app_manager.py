import time
from linkedList_wc import LinkedList
from mystack_hw import MyStack

from models.student import Student
from models.course import Course
from models.professor import Professor
from models.login_user import LoginUser
# from models.grades import Grades  

class AppManager:
    def __init__(self, csv_manager):
        """
        Load all data from CSV files using CSVManager
        and store them in LinkedLists for each entity.
        """
        self.csv_manager = csv_manager
        
        # LinkedLists for each entity
        self.students_list = LinkedList()
        self.courses_list = LinkedList()
        self.professors_list = LinkedList()
        self.logins_list = LinkedList()
        # self.grades_list = LinkedList()  

        # Populate the LinkedLists with data from CSV
        for s in self.csv_manager.load_students():
            self.students_list.add_last(s)
        for c in self.csv_manager.load_courses():
            self.courses_list.add_last(c)
        for p in self.csv_manager.load_professors():
            self.professors_list.add_last(p)
        for l in self.csv_manager.load_logins():
            self.logins_list.add_last(l)
        # for g in self.csv_manager.load_grades():
        #     self.grades_list.add_last(g)

    # ----------------------------------------------------------------
    # STUDENT OPERATIONS
    # ----------------------------------------------------------------
    def add_student(self, student_obj):
        """
        Programmatic approach: pass in a Student object, add it to the list, and save.
        """
        self.students_list.add_last(student_obj)
        self.save_all()

    def add_student_interactive(self):
        """
        Interactive approach: use Student.add_new_student() to prompt the user,
        then store the new student.
        """
        student_obj = Student.add_new_student()  # static method from Student
        self.students_list.add_last(student_obj)
        self.save_all()
        print("New student added successfully.")

    def delete_student(self, email_address):
        """
        Delete a student by email_address, returns True if found/deleted, False if not found.
        """
        current = self.students_list.head
        while current:
            if current.data.email_address == email_address:
                self.students_list.delete_node(current.data)
                self.save_all()
                return True
            current = current.next
        return False

    def delete_student_interactive(self):
        """
        Interactive approach: calls Student.delete_new_student() to get the email,
        then removes from the list if found.
        """
        email_to_delete = Student.delete_new_student()  # returns email address
        success = self.delete_student(email_to_delete)
        if success:
            print(f"Student with email {email_to_delete} deleted.")
        else:
            print(f"No student found with email {email_to_delete}.")

    def modify_student(self, email_address, new_grades, new_marks):
        """
        Modify student record by email_address, updating grades and marks.
        """
        current = self.students_list.head
        while current:
            if current.data.email_address == email_address:
                # Use the student's update_student_record() method
                current.data.update_student_record(new_grades, new_marks)
                self.save_all()
                return True
            current = current.next
        return False

    def search_student(self, email_address):
        """
        Search for a student by email_address and track search time.
        Returns the Student object or None if not found.
        """
        start_time = time.perf_counter()
        current = self.students_list.head
        while current:
            if current.data.email_address == email_address:
                end_time = time.perf_counter()
                print(f"Search time: {end_time - start_time:.6f} seconds")
                return current.data
            current = current.next
        end_time = time.perf_counter()
        print(f"Search time: {end_time - start_time:.6f} seconds")
        return None

    def sort_students_by_name(self):
        """
        Sort students by first_name using a simple approach:
        1) Convert LinkedList to a Python list
        2) Sort the list
        3) Rebuild LinkedList
        """
        student_array = []
        current = self.students_list.head
        while current:
            student_array.append(current.data)
            current = current.next
        
        # Sort by first_name
        student_array.sort(key=lambda s: s.first_name)

        # Rebuild the linked list
        self.students_list = LinkedList()
        for s in student_array:
            self.students_list.add_last(s)

    def get_course_average(self, course_id):
        """
        Compute average marks for all students in a given course.
        """
        total = 0
        count = 0
        current = self.students_list.head
        while current:
            if current.data.course_id == course_id:
                total += current.data.marks
                count += 1
            current = current.next
        return (total / count) if count > 0 else 0

    # ----------------------------------------------------------------
    # COURSE OPERATIONS
    # ----------------------------------------------------------------
    def add_course(self, course_obj):
        """
        Programmatic approach to add a Course object and save.
        """
        self.courses_list.add_last(course_obj)
        self.save_all()

    def add_course_interactive(self):
        """
        Interactive approach: calls Course.add_new_course(),
        then adds it to the list.
        """
        course_obj = Course.add_new_course()
        self.courses_list.add_last(course_obj)
        self.save_all()
        print("New course added successfully.")

    def delete_course(self, course_id):
        """
        Delete a course by course_id, returns True if found/deleted, False otherwise.
        """
        current = self.courses_list.head
        while current:
            if current.data.course_id == course_id:
                self.courses_list.delete_node(current.data)
                self.save_all()
                return True
            current = current.next
        return False

    def delete_course_interactive(self):
        """
        Interactive approach: calls Course.delete_new_course() to get the ID,
        then removes from the list if found.
        """
        course_to_delete = Course.delete_new_course()
        success = self.delete_course(course_to_delete)
        if success:
            print(f"Course with ID {course_to_delete} deleted.")
        else:
            print(f"No course found with ID {course_to_delete}.")

    def search_course(self, course_id):
        """
        Search for a course by course_id, returns the Course object or None.
        """
        current = self.courses_list.head
        while current:
            if current.data.course_id == course_id:
                return current.data
            current = current.next
        return None

    # ----------------------------------------------------------------
    # PROFESSOR OPERATIONS
    # ----------------------------------------------------------------
    def add_professor(self, professor_obj):
        """
        Programmatic approach to add a Professor object and save.
        """
        self.professors_list.add_last(professor_obj)
        self.save_all()

    def add_professor_interactive(self):
        """
        Interactive approach: calls Professor.add_new_professor(),
        then adds it to the list.
        """
        prof_obj = Professor.add_new_professor()
        self.professors_list.add_last(prof_obj)
        self.save_all()
        print("New professor added successfully.")

    def delete_professor(self, professor_email):
        current = self.professors_list.head
        while current:
            # Now that the email is stored in `professor_id`, just check that
            if current.data.professor_id == professor_email:
                self.professors_list.delete_node(current.data)
                self.save_all()
                return True
            current = current.next
        return False


    def delete_professor_interactive(self):
        """
        Interactive approach: calls Professor.delete_professor() to get the ID/email,
        then removes from the list if found.
        """
        prof_to_delete = Professor.delete_professor()  # static method
        success = self.delete_professor(prof_to_delete)
        if success:
            print(f"Professor with identifier {prof_to_delete} deleted.")
        else:
            print(f"No professor found with identifier {prof_to_delete}.")

    def modify_professor(self, professor_identifier, **kwargs):
        """
        Finds a professor by ID/email and calls modify_professor_details
        Example usage:
            modify_professor("micheal@mycsu.edu", rank="Head Professor", course_id="DATA300")
        """
        current = self.professors_list.head
        while current:
            if (hasattr(current.data, "professor_id") and current.data.professor_id == professor_identifier) or \
               (hasattr(current.data, "email_address") and current.data.email_address == professor_identifier):
                current.data.modify_professor_details(
                    professor_name=kwargs.get("name"),
                    professor_id=kwargs.get("email_address"),
                    rank=kwargs.get("rank"),
                    course_id=kwargs.get("course_id")
                )
                self.save_all()
                return True
            current = current.next
        return False

    def search_professor(self, professor_identifier):
        """
        Search for a professor by their ID/email and return the object or None.
        """
        current = self.professors_list.head
        while current:
            if (hasattr(current.data, "professor_id") and current.data.professor_id == professor_identifier) or \
               (hasattr(current.data, "email_address") and current.data.email_address == professor_identifier):
                return current.data
            current = current.next
        return None

    # ----------------------------------------------------------------
    # LOGIN (USER) OPERATIONS
    # ----------------------------------------------------------------
    def add_login_user(self, login_user_obj):
        """
        Add a new login user object to the list and save.
        """
        self.logins_list.add_last(login_user_obj)
        self.save_all()

    def validate_login(self, user_id, password):
        """
        Check if user_id/password is valid using the new LoginUser logic.
        If valid, return the user's role; otherwise None.
        """
        current = self.logins_list.head
        while current:
            if current.data.user_id == user_id:
                # Use the login() method in the updated LoginUser class
                success = current.data.login(password)
                if success:
                    # Return the role if the login was successful
                    return getattr(current.data, 'role', None)
                else:
                    return None
            current = current.next
        return None

    def change_user_password(self, user_id, new_password):
        """
        Find a user by user_id and call change_password(new_password).
        """
        current = self.logins_list.head
        while current:
            if current.data.user_id == user_id:
                current.data.change_password(new_password)
                self.save_all()
                return True
            current = current.next
        return False

    def logout_user(self, user_id):
        """
        Example method to call logout() on a given user.
        """
        current = self.logins_list.head
        while current:
            if current.data.user_id == user_id:
                current.data.logout()
                return True
            current = current.next
        return False

    # ----------------------------------------------------------------
    # SAVE ALL
    # ----------------------------------------------------------------
    def save_all(self):
        """
        Convert each LinkedList back to a list and then
        call the CSVManager save methods.
        """
        # Students
        students = []
        cur = self.students_list.head
        while cur:
            students.append(cur.data)
            cur = cur.next
        self.csv_manager.save_students(students)

        # Courses
        courses = []
        cur = self.courses_list.head
        while cur:
            courses.append(cur.data)
            cur = cur.next
        self.csv_manager.save_courses(courses)

        # Professors
        professors = []
        cur = self.professors_list.head
        while cur:
            professors.append(cur.data)
            cur = cur.next
        self.csv_manager.save_professors(professors)

        # Logins
        logins = []
        cur = self.logins_list.head
        while cur:
            logins.append(cur.data)
            cur = cur.next
        self.csv_manager.save_logins(logins)

        # grades_list = []
        # cur = self.grades_list.head
        # while cur:
        #     grades_list.append(cur.data)
        #     cur = cur.next
        # self.csv_manager.save_grades(grades_list)


