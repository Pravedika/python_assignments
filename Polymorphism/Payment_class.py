class Payment:
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("paid through upi")
class CreditCard(Payment):
    def pay(self,amount):
        print("paid through credit card")
class NetBanking(Payment):
    def pay(Self,amount):
        print("paid through net banking")
u =UPI()
c =CreditCard()
n =NetBanking()
u.pay(5600)
c.pay(4500)
n.pay(7900)