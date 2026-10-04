salaries = {
    "Ravi": 50000,
    "Priya": 60000,
    "Anu": 55000,
    "Kiran": 65000
}

total = 0
count = 0

for salary in salaries.values():
    total += salary
    count += 1

average = total / count

print("Average salary:", average)
