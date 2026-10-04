class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

students = [
    Student("Anil", 19, "CSE"),
    Student("Ravi", 20, "ECE"),
    Student("Priya", 19, "EEE")
]

for student in students:
    print(student.name, student.age, student.course)
