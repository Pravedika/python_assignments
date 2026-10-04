class Student:
    college_name = "Aditya Polytechnic College"

    def __init__(self, name):
        self.name = name

students = [Student("Anil"), Student("Ravi"), Student("Priya")]

for student in students:
    print("College:", student.college_name, "Student:", student.name)
