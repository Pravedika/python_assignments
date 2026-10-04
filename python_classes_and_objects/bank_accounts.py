class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

accounts = [
    BankAccount("Ravi", "ACC101", 10000),
    BankAccount("Priya", "ACC102", 15000)
]

for account in accounts:
    print(account.account_holder, account.account_number, account.balance)
