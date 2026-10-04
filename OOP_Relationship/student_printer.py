class Printer:
    def print_details(self, details):
        print("Printing:", details)

class Student:
    def __init__(self, name):
        self.name = name

    def print_details(self, printer):
        printer.print_details("Student Name: " + self.name)

student = Student("Ravi")
student.print_details(Printer())
