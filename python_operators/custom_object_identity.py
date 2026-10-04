class Product:
    def __init__(self, name):
        self.name = name

first = Product("Laptop")
second = Product("Laptop")
third = first

print("first == second:", first == second)
print("first is second:", first is second)
print("first is third:", first is third)
