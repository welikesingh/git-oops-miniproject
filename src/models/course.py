class Course:
    # Constructor
    def __init__(self, course_id, name, description, capacity=30):
        if not Course.is_valid_capacity(capacity):
            raise ValueError("Capacity must be a positive number")
        self.course_id = course_id
        self.name = name
        self.description = description
        self.capacity = capacity
        self.mentor = None #Connecting Course with Mentor
        self.students = [] #Connecting Course with Student
        self.enrollments = []

    # staticmethod: utility check, needs no object or class data
    @staticmethod
    def is_valid_capacity(capacity):
        return isinstance(capacity, int) and capacity > 0

    # classmethod: alternative constructor, builds a Course from "id|name|description|capacity"
    @classmethod
    def from_string(cls, data):
        course_id, name, description, capacity = data.split("|")
        return cls(course_id, name, description, int(capacity))

    def assign_mentor(self, mentor):
        self.mentor = mentor
        print(
            f"Mentor {mentor.name} assigned "
            f"to course {self.name}"
        )


    def add_enrollment(self, enrollment):
        if enrollment not in self.enrollments:
            self.enrollments.append(enrollment)


    def add_student(self, student):
        if len(self.students) >= self.capacity:
            print(f"Course {self.name} is full.")
            return False
        if student in self.students:
            print(
                f"{student.name} is already enrolled "
                f"in {self.name}."
            )
            return False
        self.students.append(student)
        print(
            f"{student.name} enrolled in "
            f"{self.name}"
        )
        return True

    def remove_student(self, student):
        if student not in self.students:
            print(
                f"{student.name} is not enrolled "
                f"in {self.name}."
            )
            return False
        self.students.remove(student)
        print(
            f"{student.name} removed from "
            f"{self.name}"
        )
        return True

    def get_available_seats(self):
        return self.capacity - len(self.students)

    def display_info(self):
        print("\n===== COURSE INFORMATION =====")
        print(f"Course ID     : {self.course_id}")
        print(f"Course Name   : {self.name}")
        print(f"Description   : {self.description}")
        print(f"Capacity      : {self.capacity}")
        if self.mentor:
            print(f"Mentor        : {self.mentor.name}")
        else:
            print("Mentor        : Not assigned")
        print(f"Enrolled      : {len(self.students)}")
        print(f"Available     : {self.get_available_seats()}")
        print( f"Enrollments   : {len(self.enrollments)}" )
