class InsufficientStockError(Exception):
    pass

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def buy(self, quantity):
        try:
            if quantity > self.stock:
                raise InsufficientStockError("Insufficient stock")

            self.stock -= quantity
            print("Purchase successful")
            print("Remaining stock:", self.stock)
        except InsufficientStockError as e:
            print("Error:", e)

product = Product("Laptop", 10)
product.buy(3)
product.buy(10)
