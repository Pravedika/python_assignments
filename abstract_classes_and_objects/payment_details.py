from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass

class UPIPayment(Payment):
    def pay(self):
        print("UPI Payment:", self.amount, "Transaction:", self.transaction_id)

class CardPayment(Payment):
    def pay(self):
        print("Card Payment:", self.amount, "Transaction:", self.transaction_id)

UPIPayment(1500, "TXN101").pay()
CardPayment(2500, "TXN102").pay()
