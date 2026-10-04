class Student:
    college_name = "Aditya Polytechnic College"

    def __init__(self, name):
        self.name = name

students = [Student("Anil"), Student("Ravi"), Student("Priya")]

for student in students:
    print(student.name, student.college_name)
