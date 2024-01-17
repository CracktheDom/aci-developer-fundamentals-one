"""
Using the Account class example from the beginning of the Week 4 module, define
a child class that represents a savings account.  Provide a means for
calculating the interest in the savings account and applying the interest to
the balance.  Add a summary method that prints the details of the account on
one line.

Write a program that processes a small number of accounts in a loop, applies
interest where applicable, and prints the account summary.

Hint:  You may need to use the isinstance() method to determine which class you
are working with.
"""


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def summary(self):
        return (
            f"Account Number: {self.account_number} Balance: ${round(self.balance, 2)}"
        )


class Savings(Account):
    def __init__(self, interest_rate: float):
        super().__init__(self, account_number, balance)
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def get_balance(self):
        return self.balance * (1 + self.interest / 100)

    def summary(self):
        return (
            f"Account Number: {self.account_number} Balance: ${round(self.balance, 2)}"
        )


def test_classes():
    her_account = Account(account_number=5486845, balance=100.52)
    his_account = Account(account_number=5486847, balance=1000.52)
    his_savings = Savings(
        Account(account_number=125487, balance=50007.32), interest_rate=6.125
    )

    print(her_account.summary())
    print(his_account.summary())
    print(her_savings.summary())


test_classes()
