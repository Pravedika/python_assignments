class UPIpayment:
    def pay(self,amount):
        print("Paid through UPI: ",amount)
class CardPayment:
    def pay(Self,amount):
        print("Paid through Card:",amount)
class CashPayment:
    def pay(self,amount):
        print("Paid through Cash:",amount)
u = UPIpayment()
c =CardPayment()
ca = CashPayment()
u.pay(3500)
c.pay(2000)
ca.pay(1500)