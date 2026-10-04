class Student:
    college_name = "Aditya Polytechnic College"

    def __init__(self, name):
        self.name = name

student_one = Student("Anil")
student_two = Student("Ravi")

print("Class variable:", Student.college_name)
print("Instance variable one:", student_one.name)
print("Instance variable two:", student_two.name)
