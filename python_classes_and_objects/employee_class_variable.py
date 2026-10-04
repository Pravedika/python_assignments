class Employee:
    company_name = "ABC Technologies"

    def __init__(self, name):
        self.name = name

employees = [Employee("Anil"), Employee("Ravi"), Employee("Priya")]

for employee in employees:
    print(employee.name, employee.company_name)
