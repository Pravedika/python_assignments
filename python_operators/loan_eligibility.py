salary = float(input("Enter monthly salary: "))
age = int(input("Enter age: "))
print("Loan eligible:", salary >= 30000 and age >= 21 and age <= 60)
