class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = [Employee("Ravi"), Employee("Sita")]

    def display(self):
        print("Department:", self.name)
        for employee in self.employees:
            print("Employee:", employee.name)

Department("IT").display()
