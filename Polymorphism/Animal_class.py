class Animal:
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        print("Woof")
class cat(Animal):
    def sound(self):
        print("Meow")
class cow(Animal):
    def sound(self):
        print("Moo")
d =dog()
c =cat()
co =cow()
d.sound()
c.sound()
co.sound()