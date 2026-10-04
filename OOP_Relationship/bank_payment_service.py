class PaymentService:
    def pay(self, amount):
        print("Payment processed:", amount)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def make_payment(self, payment_service, amount):
        payment_service.pay(amount)

account = BankAccount(10000)
account.make_payment(PaymentService(), 2000)
