from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary: 50000")

Developer("Ravi", "EMP101").calculate_salary()
