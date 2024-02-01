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
        return f"Account Number: {self.account_number} Balance: ${round(self.balance, 2):,.2f}"


class Savings(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.account_number: int = account_number
        self.balance: float = float(balance)
        self.interest_rate: float = float(interest_rate)

    def apply_interest(self):
        self.balance *= 1 + self.interest_rate / 100 / 12
        return self.balance

    def savings_summary(self):
        return f"{super().summary()} Interest Rate: {self.interest_rate}%"


# def test_classes():
#     her_account = Account(account_number=5486845, balance=100.52)
#     his_account = Account(account_number=5486847, balance=1000.52)
#     his_savings = Savings(
#         Account(account_number=125487, balance=50007.32), interest_rate=6.125
#     )

#     print(her_account.summary())
#     print(his_account.summary())
#     print(her_savings.summary())


def test_savings_object_type():
    assert isinstance(her_account, Savings)


def test_savings_account_number_exists():
    assert her_account.account_number is not None


def test_savings_account_number_type():
    assert isinstance(her_account.account_number, int)


def test_savings_balance_exists():
    assert her_account.balance is not None


def test_savings_balance_type():
    assert isinstance(her_account.balance, float)


def test_savings_interest_rate_exists():
    assert her_account.interest_rate is not None


def test_savings_interest_rate_type():
    assert isinstance(her_account.interest_rate, float)


def test_savings_interest_rate_gt_zero():
    assert her_account.interest_rate > 0


def test_apply_interest_returns_something():
    assert her_account.apply_interest() is not None


def test_apply_interest_():
    assert (
        her_account.balance * (1 + her_account.interest_rate / 100 / 12)
        == her_account.apply_interest()
    )


def test_savings_summary_returns_output():
    assert her_account.summary() is not None


def test_savings_summary():
    assert (
        her_account.savings_summary()
        == f"{her_account.summary()}, Interest Rate: {her_account.interest_rate}%"
    )


her_account = Savings(12345, 1500, 4.375)
print(her_account.savings_summary())

# if __name__ == "__main__":
#     test_classes()
