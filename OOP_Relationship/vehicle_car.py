class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

car = Car()
car.move()
car.drive()
