class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

student = Student("Pravedika", 20, "CSE", 85)
print(student.name, student.age, student.course, student.marks)
