try:
    salary = float(input("enter the employee salary: "))
    if salary < 0:
        raise ValueError("Salary must be in positive")
except ValueError as e:
    print("Error: ",e)