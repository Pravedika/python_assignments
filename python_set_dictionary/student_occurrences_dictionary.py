students = ["Ravi", "Priya", "Ravi", "Anu", "Priya", "Ravi", "Kiran"]

frequency = {}

for student in students:
    if student in frequency:
        frequency[student] += 1
    else:
        frequency[student] = 1

print(frequency)
