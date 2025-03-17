import csv
import os

from models.student import Student
from models.course import Course
from models.professor import Professor
from models.login_user import LoginUser

class CSVManager:
    def __init__(self, base_path="data"):
        self.base_path = base_path

    # ----------------------------------------------------------------
    # STUDENTS
    # ----------------------------------------------------------------
    def load_students(self):
        """
        Reads student records from student.csv and returns a list of Student objects.
        The columns are (per original instructions):
            Email_address, First name, Last name, Course.id, grades, Marks
        """
        students = []
        file_path = os.path.join(self.base_path, "student.csv")
        if not os.path.exists(file_path):
            return students  # Return empty if file does not exist
        
        with open(file_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Matching the exact column names from your instructions
                email_address = row["Email_address"]
                first_name = row["First name"]
                last_name = row["Last name"]
                course_id = row["Course.id"]       # note the dot in "Course.id"
                grades = row["grades"]
                marks = float(row["Marks"])        # or int, depending on your data
                
                # Create a Student object (adapt to your constructor)
                student_obj = Student(
                    email_address,
                    first_name,
                    last_name,
                    course_id,
                    grades,
                    marks
                )
                students.append(student_obj)
        return students

    def save_students(self, students):
        """
        Writes a list of Student objects to student.csv.
        Maintains the same column order and names:
            Email_address, First name, Last name, Course.id, grades, Marks
        """
        file_path = os.path.join(self.base_path, "student.csv")
        fieldnames = [
            "Email_address", 
            "First name", 
            "Last name", 
            "Course.id", 
            "grades", 
            "Marks"
        ]
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow({
                    "Email_address": s.email_address,
                    "First name": s.first_name,
                    "Last name": s.last_name,
                    "Course.id": s.course_id,
                    "grades": s.grades,
                    "Marks": s.marks
                })

    # ----------------------------------------------------------------
    # COURSES
    # ----------------------------------------------------------------
    def load_courses(self):
        """
        Reads course records from course.csv and returns a list of Course objects.
        The columns are (per original instructions):
            Course.id, Course_name, Description
        """
        courses = []
        file_path = os.path.join(self.base_path, "course.csv")
        if not os.path.exists(file_path):
            return courses
        
        with open(file_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                course_id = row["Course.id"]       # note the dot in "Course.id"
                course_name = row["Course_name"]
                description = row["Description"]
                
                # Create a Course object (adapt to your constructor)
                course_obj = Course(course_id, course_name, description)
                courses.append(course_obj)
        return courses

    def save_courses(self, courses):
        """
        Writes a list of Course objects to course.csv.
        Maintains the same column order and names:
            Course.id, Course_name, Description
        """
        file_path = os.path.join(self.base_path, "course.csv")
        fieldnames = ["Course.id", "Course_name", "Description"]
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for c in courses:
                writer.writerow({
                    "Course.id": c.course_id,
                    "Course_name": c.course_name,
                    "Description": c.credits  # or c.description, depending on your constructor
                })

    # ----------------------------------------------------------------
    # PROFESSORS
    # ----------------------------------------------------------------
    def load_professors(self):
        """
        Reads professor records from professor.csv and returns a list of Professor objects.
        The columns are (per original instructions):
            Professor_id, Professor Name, Rank, Course.id
        Example row:
            micheal@mycsu.edu, Michael John, Senior Professor, DATA200
        """
        professors = []
        file_path = os.path.join(self.base_path, "professor.csv")
        if not os.path.exists(file_path):
            return professors
        
        with open(file_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                professor_id = row["Professor_id"]
                professor_name = row["Professor Name"]
                rank = row["Rank"]
                course_id = row["Course.id"]   # note the dot in "Course.id"
                
                # Create a Professor object (adapt to your constructor)
                # If your Professor constructor is (prof_id, name, rank, course_id), do:
                prof_obj = Professor(professor_id, professor_name, rank, course_id)
                professors.append(prof_obj)
        return professors

    def save_professors(self, professors):
        """
        Writes a list of Professor objects to professor.csv.
        Maintains the same column order and names:
            Professor_id, Professor Name, Rank, Course.id
        """
        file_path = os.path.join(self.base_path, "professor.csv")
        fieldnames = ["Professor_id", "Professor Name", "Rank", "Course.id"]
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in professors:
                writer.writerow({
                    "Professor_id": p.professor_id,
                    "Professor Name": p.professor_name,
                    "Rank": p.rank,
                    "Course.id": p.course_id
                })

    # ----------------------------------------------------------------
    # LOGIN USERS
    # ----------------------------------------------------------------
    def load_logins(self):
        """
        Reads login records from login.csv and returns a list of LoginUser objects.
        The columns are (per original instructions):
            User_id, Password, Role
        Password is stored encrypted in the file, so we decrypt before constructing.
        """
        logins = []
        file_path = os.path.join(self.base_path, "login.csv")
        if not os.path.exists(file_path):
            return logins
        
        with open(file_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = row["User_id"]
                encrypted_password = row["Password"]
                role = row["Role"]
                
                # Decrypt using the static method from your updated LoginUser class
                decrypted_pass = LoginUser.decrypt_password(encrypted_password)
                
                # Create a LoginUser object (adapt to your constructor if it includes 'role')
                login_obj = LoginUser(user_id, decrypted_pass, role)
                logins.append(login_obj)
        return logins

    def save_logins(self, logins):
        """
        Writes a list of LoginUser objects to login.csv.
        Maintains the same column order and names:
            User_id, Password, Role
        We encrypt the password before writing to file.
        """
        file_path = os.path.join(self.base_path, "login.csv")
        fieldnames = ["User_id", "Password", "Role"]
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for l in logins:
                # l.password is the *decrypted* version in memory
                # l._encrypted_password is the internal encrypted version
                # We'll re-encrypt to ensure it matches the format
                enc_pass = LoginUser.encrypt_password(l.password)
                
                writer.writerow({
                    "User_id": l.user_id,
                    "Password": enc_pass,
                    "Role": l.role
                })

