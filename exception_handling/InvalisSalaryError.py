class InvalidSalaryError(Exception):
    pass
try:
    max_salary = float(input("enter the maximum salary: "))
    salary = float(input("enter the salary: "))
    if salary > max_salary:
        raise  InvalidSalaryError("Invalid Salary")
    print("Valid Salary")
except InvalidSalaryError as e:
    print("Error: ",e)
