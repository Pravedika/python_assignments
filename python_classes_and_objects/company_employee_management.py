class Employee:
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [
            employee for employee in self.employees
            if employee.employee_id != employee_id
        ]

    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def display_employees(self):
        for employee in self.employees:
            print(employee.employee_id, employee.name, employee.department)

company = Company()

company.add_employee(Employee(101, "Anil", "IT"))
company.add_employee(Employee(102, "Ravi", "HR"))
company.add_employee(Employee(103, "Priya", "Finance"))

print("Employees:")
company.display_employees()

found = company.search_employee(102)
if found:
    print("Found:", found.name, found.department)

company.remove_employee(101)

print("After removal:")
company.display_employees()
