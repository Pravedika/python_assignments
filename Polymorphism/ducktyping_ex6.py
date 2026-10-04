class Dog:
    def sound(self):
        print("Dog barks Bow-Bow")
class Cat:
    def sound(self):
        print("Cat sounds like Meow-Meow")
class Cow:
    def sound(self):
        print("Cow sounds like Moo-Moo")
def show(animal):
    animal.sound()
d=Dog()
c1=Cat()
c2=Cow()
show(d)
show(c1)
show(c2)
