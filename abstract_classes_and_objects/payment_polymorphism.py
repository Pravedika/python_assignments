from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Processing UPI payment.")

class Card(Payment):
    def pay(self):
        print("Processing Card payment.")

class NetBanking(Payment):
    def pay(self):
        print("Processing Net Banking payment.")

payments = [UPI(), Card(), NetBanking()]

for payment in payments:
    payment.pay()
