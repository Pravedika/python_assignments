class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

employee = Employee("Ravi", 40000)
employee.display_salary()
