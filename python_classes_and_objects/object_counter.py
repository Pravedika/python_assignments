class Student:
    object_count = 0

    def __init__(self, name):
        self.name = name
        Student.object_count += 1

students = [Student("Anil"), Student("Ravi"), Student("Priya")]

print("Total objects:", Student.object_count)
