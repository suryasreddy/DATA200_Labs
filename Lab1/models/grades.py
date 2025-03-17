class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def display_grade_report(self):
        """
        Displays the grade report.
        """
        print("\n=== Grade Report ===")
        print(f"Grade ID    : {self.grade_id}")
        print(f"Grade       : {self.grade}")
        print(f"Marks Range : {self.marks_range}")

    @staticmethod
    def add_grade():
        """
        Prompts the user to enter new grade details and returns a Grades object.
        """
        print("\n=== Add New Grade ===")
        grade_id = input("Enter Grade ID: ")
        grade = input("Enter Grade (e.g., A, B, C): ")
        marks_range = input("Enter Marks Range (e.g., 90-100): ")
        return Grades(grade_id, grade, marks_range)

    @staticmethod
    def delete_grade():
        """
        Prompts the user for a grade ID to delete a grade record.
        Returns the grade ID so a manager or caller can handle the actual deletion.
        """
        print("\n=== Delete Grade ===")
        grade_id = input("Enter Grade ID to delete: ")
        return grade_id

    def modify_grade(self, grade=None, marks_range=None):
        """
        Modifies the grade or marks range (or both).
        If a parameter is None, that field remains unchanged.
        """
        if grade is not None:
            self.grade = grade
        if marks_range is not None:
            self.marks_range = marks_range

    def __str__(self):
        """
        String representation of the Grades object.
        """
        return (f"Grades(grade_id={self.grade_id}, grade={self.grade}, "
                f"marks_range={self.marks_range})")
