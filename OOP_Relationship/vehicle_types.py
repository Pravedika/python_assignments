class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding.")

class Bus(Vehicle):
    def transport(self):
        print("Bus is transporting passengers.")

Car().move()
Car().drive()
Bike().move()
Bike().ride()
Bus().move()
Bus().transport()
