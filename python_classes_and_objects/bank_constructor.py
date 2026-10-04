class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account = BankAccount("Pravedika", "ACC1001", 15000)
print(account.account_holder, account.account_number, account.balance)
