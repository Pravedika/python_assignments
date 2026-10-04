class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

account = BankAccount("Pravedika", "ACC1001")
print("Account Holder:", account.account_holder)
print("Account Number:", account.account_number)
