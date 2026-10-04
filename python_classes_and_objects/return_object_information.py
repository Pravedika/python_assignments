class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class College:
    def __init__(self, student):
        self.student = student

    def get_student(self):
        return self.student

student = Student("Pravedika", 20)
college = College(student)

result = college.get_student()
print("Name:", result.name)
print("Age:", result.age)
