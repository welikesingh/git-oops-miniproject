from src.models.user import User


class Mentor(User):

    def __init__(self, name, email, expertise):
        super().__init__(name, email)

        self.expertise = expertise
        self.assigned_students = []

    def assign_student(self, student):
        self.assigned_students.append(student)
        print( f"{student.name} assigned to mentor {self.name}" )

    # polymorphism
    def display_role(self):
        return "Mentor"

    def display_info(self):
        super().display_info()
        print(f"Expertise: {self.expertise}")
        print(
            f"Assigned Students: "
            f"{len(self.assigned_students)}"
        )