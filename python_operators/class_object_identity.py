class Student:
    pass

first = Student()
second = Student()
third = first

print("First and second are same:", first is second)
print("First and third are same:", first is third)
