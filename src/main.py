from src.models.user import User
from src.models.student import Student
from src.models.mentor import Mentor
from src.models.course import Course

def main():

    student1 = Student(
        "John",
        "john@example.com",
        "Python Programming"
    )

    student2 = Student(
        "Sarah",
        "sarah@example.com",
        "Python Programming"
    )

    mentor = Mentor(
        "Alice",
        "alice@example.com",
        "Python and AI"
    )

    # Create course
    course = Course(
        "PY101",
        "Python Programming",
        "Learn Python programming and OOP",
        30
    )


    # Assign mentor to course
    course.assign_mentor(mentor)
    
    # Enroll student
    course.add_student(student1)
    course.add_student(student2)

    mentor.assign_student(student1)
    mentor.assign_student(student2)


    student1.complete_assignment("Assignment 1")
    student2.complete_assignment("Assignment 2")


    print("===== STUDENT =====")
    student1.display_info()
    student2.display_info()

    print()

    print("===== MENTOR =====")
    mentor.display_info()

    print()

    print("===== COURSE =====")
    course.display_info()


 

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
    student1.email = "newemail@example.com"
    print("Email updated to:", student1.email)
    try:
        student1.email = "invalid-email"
    except ValueError as error:
        print("Encapsulation:", error)

    print("===== POLYMORPHISM ====")
    # Same method call display_role() works differently for each object
    users = [student1, mentor]
    for user in users:
        print(f"{user.name} -> {user.display_role()}")

if __name__ == "__main__":
    main()

    