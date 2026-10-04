class BankAccount:
    bank_name = "State Bank"

    def __init__(self, holder, number):
        self.holder = holder
        self.number = number

accounts = [
    BankAccount("Ravi", "101"),
    BankAccount("Priya", "102")
]

for account in accounts:
    print(account.holder, account.number, account.bank_name)
