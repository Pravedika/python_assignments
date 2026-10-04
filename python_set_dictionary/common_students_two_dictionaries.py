python_marks = {
    "Ravi": 80,
    "Priya": 90,
    "Anu": 75
}

java_marks = {
    "Priya": 85,
    "Anu": 88,
    "Kiran": 70
}

common_students = set(python_marks.keys()).intersection(java_marks.keys())

print(common_students)
