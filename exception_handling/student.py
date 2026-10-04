class InvalidMarksError(Exception):
    pass

class Student:
    def __init__(self, name, marks):
        try:
            if marks < 0 or marks > 100:
                raise InvalidMarksError("Marks must be between 0 and 100")

            self.name = name
            self.marks = marks
            print("Student:", self.name)
            print("Marks:", self.marks)
        except InvalidMarksError as e:
            print("Error:", e)

Student("Ravi", 85)
Student("Priya", 120)
