marks = [float(input(f"Enter marks for subject {i}: ")) for i in range(1, 4)]
total = sum(marks)
average = total / len(marks)
percentage = total / (len(marks) * 100) * 100

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

passed = all(mark >= 35 for mark in marks)

print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Grade:", grade)
print("Pass:", passed)
