class PaymentService:
    def pay(self, amount):
        print("Payment completed:", amount)

class Order:
    def checkout(self, payment_service):
        payment_service.pay(1500)

Order().checkout(PaymentService())

print("Relationship: USES-A")
