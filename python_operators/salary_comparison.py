salary_one = float(input("Enter first salary: "))
salary_two = float(input("Enter second salary: "))
if salary_one > salary_two:
    print("First salary is greater.")
elif salary_two > salary_one:
    print("Second salary is greater.")
else:
    print("Both salaries are equal.")
