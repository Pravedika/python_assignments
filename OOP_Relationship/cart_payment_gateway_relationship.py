class PaymentGateway:
    def pay(self, amount):
        print("Payment processed:", amount)

class ShoppingCart:
    def checkout(self, gateway):
        gateway.pay(2500)

ShoppingCart().checkout(PaymentGateway())

print("Relationship: USES-A")
