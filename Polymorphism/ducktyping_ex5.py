class UPIPayment:
    def  pay(self):
        print("we provide UPI payment service")
class CardPayment:
    def pay(self):
        print("we provide card payment service")
def show(payment):
    payment.pay()
u=UPIPayment()
c=CardPayment()
show(u)
show(c)