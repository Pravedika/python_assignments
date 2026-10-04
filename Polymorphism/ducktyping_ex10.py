class DebitCard:
    def pay(self):
        print("Ammount is deducted immediately")
class CreditCard:
    def pay(self):
        print("you pay the bill later")
def show(report):
    report.pay()
e=DebitCard()
p=CreditCard()
show(e)
show(p)