from src.models.user import User
from src.models.student import Student
from src.models.mentor import Mentor
from src.models.course import Course
from src.models.enrollment import Enrollment
def main():

    # -------------------------
    # Create Student
    # -------------------------

    student = Student(
        "John",
        "john@example.com"
    )

    # -------------------------
    # Create Mentor
    # -------------------------

    mentor = Mentor(
        "Alice",
        "alice@example.com",
        "Python and AI"
    )

    # -------------------------
    # Create Course
    # -------------------------

    course = Course(
        "PY101",
        "Python Programming",
        "Learn Python programming and OOP",
        30
    )

    # -------------------------
    # Assign Mentor
    # -------------------------

    course.assign_mentor(mentor)

    # -------------------------
    # Add Student to Course
    # -------------------------

    course.add_student(student)

    # -------------------------
    # Create Enrollment
    # -------------------------

    enrollment = Enrollment(
        student,
        course
    )

    # -------------------------
    # Connect Enrollment
    # -------------------------

    student.add_enrollment(enrollment)

    course.add_enrollment(enrollment)

    # -------------------------
    # Display Information
    # -------------------------

    student.display_info()

    course.display_info()

    enrollment.display_info()

    # -------------------------
    # Complete Enrollment
    # -------------------------

    print("\nCompleting enrollment...")

    enrollment.complete()

 

    print("===== OTHER OPERATIONS =====")
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

    