class Printer:
    def print_details(self, name):
        print("Printing student:", name)

class Student:
    def __init__(self, name):
        self.name = name

    def print_student(self, printer):
        printer.print_details(self.name)

Student("Ravi").print_student(Printer())

print("Relationship: USES-A")
