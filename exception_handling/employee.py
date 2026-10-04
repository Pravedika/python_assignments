class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        try:
            if salary <= 0:
                raise InvalidSalaryError("Salary must be greater than zero")

            self.name = name
            self.salary = salary
            print("Employee:", self.name)
            print("Salary:", self.salary)
        except InvalidSalaryError as e:
            print("Error:", e)

Employee("Ravi", 30000)
Employee("Priya", -5000)
