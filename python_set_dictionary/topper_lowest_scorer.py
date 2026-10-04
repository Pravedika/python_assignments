marks = {
    "Ravi": 80,
    "Priya": 95,
    "Anu": 70,
    "Kiran": 88,
    "Sita": 65
}

topper = None
lowest = None
highest_marks = None
lowest_marks = None

for student, mark in marks.items():
    if highest_marks is None or mark > highest_marks:
        highest_marks = mark
        topper = student

    if lowest_marks is None or mark < lowest_marks:
        lowest_marks = mark
        lowest = student

print("Topper:", topper, highest_marks)
print("Lowest scorer:", lowest, lowest_marks)
