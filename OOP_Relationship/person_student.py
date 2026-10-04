class Person:
    def introduce(self):
        print("I am a person.")

class Student(Person):
    def study(self):
        print("Student is studying.")

student = Student()
student.introduce()
student.study()
