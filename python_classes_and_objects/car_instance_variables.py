class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

cars = [
    Car("Toyota", "Camry", 2024, 30000),
    Car("Honda", "City", 2023, 18000),
    Car("BMW", "X3", 2025, 55000)
]

for car in cars:
    print(car.brand, car.model, car.year, car.price)
