class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

student = Student("Pravedika", [80, 75, 90, 85])
print("Total:", student.total_marks())
print("Average:", student.average_marks())
