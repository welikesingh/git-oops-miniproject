from src.models.user import User
from src.models.student import Student
from src.models.mentor import Mentor


def main():

    student = Student(
        "John",
        "john@example.com",
        "Python Programming"
    )

    mentor = Mentor(
        "Alice",
        "alice@example.com",
        "Python and AI"
    )

    print("===== STUDENT =====")
    student.display_info()

    print()

    print("===== MENTOR =====")
    mentor.display_info()

    print()

    print("===== OTHER OPERATIONS =====")

    student.complete_assignment("Assignment 1")
    student.complete_assignment("Assignment 2")

    mentor.assign_student(student)

    print()

    print("Total users:", Student.get_total_users())


    print("===== TEST STATIC METHODS =====")
    ## Test @staticmethod (called on class, no object needed)
    print("Is 'abc@test.com' valid?", User.is_valid_email("abc@test.com"))



    print("===== TEST ABSTRACTION/ENCAPSULATION BEHAVIOUR =====")
    ## Test abstraction: abstract class cannot be created directly
    try:
        User("Test", "test@example.com")
    except TypeError as error:
        print("Abstraction:", error)

    ## Test encapsulation
    student.email = "newemail@example.com"
    print("Email updated to:", student.email)
    try:
        student.email = "invalid-email"
    except ValueError as error:
        print("Encapsulation:", error)

    print("===== POLYMORPHISM ====")
    # Same method call display_role() works differently for each object
    users = [student, mentor]
    for user in users:
        print(f"{user.name} -> {user.display_role()}")

if __name__ == "__main__":
    main()

    