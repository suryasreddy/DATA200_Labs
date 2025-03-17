class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def display_course(self):
        """
        Displays the course information.
        """
        print("\n=== Course Information ===")
        print(f"Course ID   : {self.course_id}")
        print(f"Course Name : {self.course_name}")
        print(f"Credits     : {self.credits}")

    @staticmethod
    def add_new_course():
        """
        Prompts the user to enter new course details and returns a Course object.
        """
        print("\n=== Add New Course ===")
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        credits = input("Enter course credits: ")
        return Course(course_id, course_name, credits)

    @staticmethod
    def delete_new_course():
        """
        Prompts the user for a course ID to delete a course record.
        Returns the course ID so a manager or caller can handle the actual deletion.
        """
        print("\n=== Delete Course ===")
        course_id = input("Enter the Course ID to delete: ")
        return course_id

    def __str__(self):
        """
        String representation of the Course object.
        """
        return (f"Course(course_id={self.course_id}, course_name={self.course_name}, "
                f"credits={self.credits})")
