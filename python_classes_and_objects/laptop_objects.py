class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

laptops = [
    Laptop("Dell", "8GB", "512GB", 60000),
    Laptop("HP", "16GB", "1TB", 75000),
    Laptop("Lenovo", "16GB", "512GB", 70000)
]

for laptop in laptops:
    print(laptop.brand, laptop.ram, laptop.storage, laptop.price)
