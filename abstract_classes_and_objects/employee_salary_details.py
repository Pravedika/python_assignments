from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_details(self):
        print("Manager:", self.name, "Salary:", self.calculate_salary())

class Developer(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_details(self):
        print("Developer:", self.name, "Salary:", self.calculate_salary())

Manager("Ravi", 60000).display_details()
Developer("Sita", 50000).display_details()
