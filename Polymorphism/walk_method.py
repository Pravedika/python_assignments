class Duck:
    def walk(Self):
        print("Duck is walking")
class Dog:
    def walk(Self):
        print("dog is walking")
def make_walk(animal):
    animal.walk()
d1 = Duck()
d2 = Dog()
make_walk(d1)
make_walk(d2)