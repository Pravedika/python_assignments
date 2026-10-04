class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

student_one = Student("Anil")
student_two = Student("Ravi")
student_three = Student("Priya")

print("Students created:", Student.count)
