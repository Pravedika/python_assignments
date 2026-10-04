class BankAccount:
    def show(self,name,number):
        self.name=name
        self.number=number
    def display(self):
        print("Holder Name: ",self.name)
        print("Account Number: ",self.number)
b =BankAccount()
b.show("devi",38170053)
b.display()