class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

cars = [Car("Camry", 30000), Car("Corolla", 25000)]

for car in cars:
    print(car.company, car.number_of_wheels, car.model, car.price)
