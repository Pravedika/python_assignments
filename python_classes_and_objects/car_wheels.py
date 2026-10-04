class Car:
    number_of_wheels = 4

    def __init__(self, brand):
        self.brand = brand

cars = [Car("Toyota"), Car("Honda"), Car("BMW")]

for car in cars:
    print(car.brand, car.number_of_wheels)
