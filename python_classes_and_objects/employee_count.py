class Employee:
    company_name = "ABC Technologies"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

employees = [Employee("Anil"), Employee("Ravi"), Employee("Priya")]

print("Company:", Employee.company_name)
print("Employees:", Employee.employee_count)
