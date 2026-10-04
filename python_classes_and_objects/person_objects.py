class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

people = [
    Person("Ravi", 20, "Kakinada"),
    Person("Priya", 21, "Rajahmundry")
]

for person in people:
    print(person.name, person.age, person.city)
