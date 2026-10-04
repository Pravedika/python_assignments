from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display(self):
        pass

class Student(Person):
    def display(self):
        print("Student:", self.name, "Age:", self.age)

class Teacher(Person):
    def display(self):
        print("Teacher:", self.name, "Age:", self.age)

class Doctor(Person):
    def display(self):
        print("Doctor:", self.name, "Age:", self.age)

for person in [
    Student("Anu", 20),
    Teacher("Ravi", 35),
    Doctor("Kumar", 40)
]:
    person.display()
