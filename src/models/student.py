from src.models.user import User


class Student(User):

    def __init__(self, name, email, course_name):
        super().__init__(name, email)

        self.course_name = course_name
        self.completed_assignments = []

    def enroll(self, course_name):
        self.course_name = course_name
        print(f"{self.name} enrolled in {course_name}")

    def complete_assignment(self, assignment):
        self.completed_assignments.append(assignment)
        print(f"{self.name} completed: {assignment}")

    # polymorphism
    def display_role(self):
        return "Student"

    def display_info(self):
        super().display_info()
        print(f"Course  : {self.course_name}")
        print(
            f"Completed Assignments: "
            f"{len(self.completed_assignments)}"
        )