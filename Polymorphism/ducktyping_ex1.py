class Car:
    def start(self):
        print("car is started")
class Bike:
    def start(self):
        print("Bike is started")
def show(veh):
    veh.start()
c =Car()
b = Bike()
show(c)
show(b)
