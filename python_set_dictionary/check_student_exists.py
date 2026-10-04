marks = {
    "Ravi": 80,
    "Priya": 90,
    "Anu": 75
}

name = input("Enter student name: ")

if name in marks:
    print("Student exists")
else:
    print("Student does not exist")
