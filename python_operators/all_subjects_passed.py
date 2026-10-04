subjects = [float(input("Enter subject marks: ")) for _ in range(3)]
passed = all(mark >= 35 for mark in subjects)
print("Passed all subjects:", passed)
