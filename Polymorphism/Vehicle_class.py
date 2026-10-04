class Vehicle:
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Starts")
class Bike(Vehicle):
    def start(self):
        print("Bike Starts")
class Bus(Vehicle):
    def start(self):
        print("Bus Starts")
c1 =Car()
b1 =Bike()
b2 =Bus()
c1.start()
b1.start()
b2.start()
