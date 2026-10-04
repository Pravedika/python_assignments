class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car_one = Car("Toyota", "Camry", 30000)
car_two = Car("Honda", "City", 18000)
car_three = Car("BMW", "X3", 55000)

for car in [car_one, car_two, car_three]:
    print(car.brand, car.model, car.price)
