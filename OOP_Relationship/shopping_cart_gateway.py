class PaymentGateway:
    def process_payment(self, amount):
        print("Payment processed:", amount)

class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def checkout(self, gateway):
        gateway.process_payment(self.total)

cart = ShoppingCart(5000)
cart.checkout(PaymentGateway())
