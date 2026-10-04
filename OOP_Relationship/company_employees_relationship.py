class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.employees = [Employee("Ravi"), Employee("Sita")]

    def display_employees(self):
        for employee in self.employees:
            print("Employee:", employee.name)

Company().display_employees()

print("Relationship: HAS-A")
