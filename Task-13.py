class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = 0

    def replenish(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Недостаточно средств на счету')
        return self.balance