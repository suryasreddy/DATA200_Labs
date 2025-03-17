class Professor:
    def __init__(self, professor_id, professor_name, rank, course_id):
        """
        professor_id: The professor's unique ID (which you want to be the email address)
        professor_name: The professor's name (e.g., 'Michael John')
        rank: The professor's rank (e.g., 'Senior Professor')
        course_id: The course they are assigned to (e.g., 'DATA200')
        """
        self.professor_id = professor_id
        self.professor_name = professor_name
        self.rank = rank
        self.course_id = course_id

    def professors_details(self):
        """
        Prints the professor's details.
        """
        print("\n=== Professor Details ===")
        print(f"Professor ID (Email) : {self.professor_id}")
        print(f"Professor Name       : {self.professor_name}")
        print(f"Rank                 : {self.rank}")
        print(f"Course ID            : {self.course_id}")

    @staticmethod
    def add_new_professor():
        """
        Prompts the user to enter new professor details and returns a Professor object.
        """
        print("\n=== Add New Professor ===")
        professor_id = input("Enter Professor Email Address: ")
        professor_name = input("Enter Professor Name: ")
        rank = input("Enter Rank: ")
        course_id = input("Enter Course ID: ")
        return Professor(professor_id, professor_name, rank, course_id)

    @staticmethod
    def delete_professor():
        """
        Prompts the user for a professor identifier (e.g., email) to delete a professor record.
        Returns that identifier so a manager or caller can handle the actual deletion.
        """
        print("\n=== Delete Professor ===")
        prof_id = input("Enter the Professor's Email (Professor_id) to delete: ")
        return prof_id

    def modify_professor_details(self, professor_name=None, professor_id=None, rank=None, course_id=None):
        """
        Modifies the professor's details. If a parameter is None, that field remains unchanged.
        """
        if professor_name is not None:
            self.professor_name = professor_name
        if professor_id is not None:
            self.professor_id = professor_id
        if rank is not None:
            self.rank = rank
        if course_id is not None:
            self.course_id = course_id

    def show_course_details_by_professor(self):
        """
        Displays which course the professor is assigned to.
        """
        print(f"\nProfessor {self.professor_name} (Rank: {self.rank}) is assigned to Course ID: {self.course_id}")

    def __str__(self):
        """
        String representation of the Professor object.
        """
        return (f"Professor(ID={self.professor_id}, Name={self.professor_name}, "
                f"Rank={self.rank}, CourseID={self.course_id})")

