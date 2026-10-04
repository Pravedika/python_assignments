employees = {
    "Ravi": 45000,
    "Priya": 60000,
    "Anu": 55000,
    "Kiran": 48000
}

for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)
