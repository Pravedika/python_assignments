marks = {
    "Ravi": 80,
    "Priya": 95,
    "Anu": 88,
    "Kiran": 92
}

highest_student = None
highest_marks = None

for student, mark in marks.items():
    if highest_marks is None or mark > highest_marks:
        highest_marks = mark
        highest_student = student

print("Student with highest marks:", highest_student)
print("Marks:", highest_marks)
