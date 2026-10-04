class EnrollmentError(Exception):
    pass

class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def enroll(self, student):
        try:
            if student in self.students:
                raise EnrollmentError("Student is already enrolled")

            if len(self.students) >= self.capacity:
                raise EnrollmentError("Course is full")

            self.students.append(student)
            print(student, "enrolled successfully")
        except EnrollmentError as e:
            print("Error:", e)

course = Course("Python", 2)
course.enroll("Ravi")
course.enroll("Priya")
course.enroll("Arun")
course.enroll("Ravi")
