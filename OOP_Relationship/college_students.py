class Student:
    def __init__(self, name):
        self.name = name

class College:
    def __init__(self):
        self.students = [Student("Ravi"), Student("Sita"), Student("Kumar")]

    def display_students(self):
        for student in self.students:
            print("Student:", student.name)

College().display_students()
