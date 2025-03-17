class Student:
    def __init__(self, email_address, first_name, last_name, course_id, grades, marks):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grades = grades
        self.marks = marks

    def display_records(self):
        """
        Displays the student's record information.
        """
        print("\n=== Student Record ===")
        print(f"Email Address : {self.email_address}")
        print(f"First Name    : {self.first_name}")
        print(f"Last Name     : {self.last_name}")
        print(f"Course ID     : {self.course_id}")
        print(f"Grades        : {self.grades}")
        print(f"Marks         : {self.marks}")

    @staticmethod
    def add_new_student():
        """
        Prompts the user to enter new student details and returns a Student object.
        """
        print("\n=== Add New Student ===")
        email_address = input("Enter email address: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        course_id = input("Enter course ID: ")
        grades = input("Enter grades (e.g., A/B/C): ")
        marks = float(input("Enter marks: "))
        return Student(email_address, first_name, last_name, course_id, grades, marks)

    @staticmethod
    def delete_new_student():
        """
        Prompts the user for an email address to delete a student record.
        Returns the email address so a manager or caller can handle the actual deletion.
        """
        print("\n=== Delete Student ===")
        email_address = input("Enter the email address of the student to delete: ")
        return email_address

    def check_my_grades(self):
        """
        Returns the student's grades.
        """
        return self.grades

    def check_my_marks(self):
        """
        Returns the student's marks.
        """
        return self.marks

    def update_student_record(self, new_grades, new_marks):
        """
        Updates the student's grades and marks.
        """
        self.grades = new_grades
        self.marks = new_marks

    def __str__(self):
        """
        String representation of the Student object.
        """
        return (f"Student(email={self.email_address}, first_name={self.first_name}, "
                f"last_name={self.last_name}, course_id={self.course_id}, "
                f"grades={self.grades}, marks={self.marks})")
