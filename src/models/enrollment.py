from datetime import datetime


class Enrollment:

    VALID_STATUSES = {
        "Active",
        "Completed",
        "Cancelled"
    }

    enrollment_count = 0

    def __init__(self, student, course):
        Enrollment.enrollment_count += 1

        self.enrollment_id = Enrollment.enrollment_count
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()
        self.status = "Active"

    def complete(self):
        self.status = "Completed"

        print(
            f"Enrollment {self.enrollment_id} "
            f"marked as completed."
        )

    def cancel(self):
        self.status = "Cancelled"

        print(
            f"Enrollment {self.enrollment_id} "
            f"cancelled."
        )

    def is_active(self):
        return self.status == "Active"

    def display_info(self):

        print("\n===== ENROLLMENT INFORMATION =====")

        print(f"Enrollment ID : {self.enrollment_id}")
        print(f"Student       : {self.student.name}")
        print(f"Course        : {self.course.name}")
        print(
            f"Enrollment Date: "
            f"{self.enrollment_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print(f"Status        : {self.status}")