class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employees = [
    Employee("A", "IT", 30000),
    Employee("B", "HR", 35000),
    Employee("C", "Sales", 40000),
    Employee("D", "Finance", 45000),
    Employee("E", "IT", 50000)
]

for employee in employees:
    print(employee.name, employee.department, employee.salary)
