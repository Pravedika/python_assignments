class Employee:
    def calculate_salary(self,amount):
        pass
class manager(Employee):
    def calculate_salary(self,amount):
        print("Manager Salary: ",amount)
class Developer(Employee):
    def calculate_salary(self,amount):
        print("Developer salary: ",amount)
m =  manager()
d =Developer()
m.calculate_salary(65000)
d.calculate_salary(50000)

