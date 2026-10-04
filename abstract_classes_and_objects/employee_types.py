from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def display(self):
        pass

class Manager(Employee):
    def display(self):
        print("Manager:", self.name, "Salary:", self.salary)

class Developer(Employee):
    def display(self):
        print("Developer:", self.name, "Salary:", self.salary)

class Tester(Employee):
    def display(self):
        print("Tester:", self.name, "Salary:", self.salary)

for employee in [
    Manager("Ravi", 60000),
    Developer("Sita", 50000),
    Tester("Kumar", 45000)
]:
    employee.display()
