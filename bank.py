class Bank(object):
        def __init__(self):
            self.balance = 135

        def withdraw(self, amount):
            if amount >= self.balance:
                amount = self.balance
            self.balance = self.balance - amount
            return amount

        def deposit(self, amount):
            self.balance = self.balance + amount
