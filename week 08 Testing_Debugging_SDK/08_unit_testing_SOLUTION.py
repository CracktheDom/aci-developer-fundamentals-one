"""
Modify the accounts.py program from the section on Classes and Objects by adding unit tests for the Account and SavingsAccount classes.  
Verify the following: 
 - The constructor for each class assigns all values correctly
 - Functions return the proper values or modify other member variables appropriately
"""

import unittest


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


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += (self.balance * self.interest_rate) / 12

    def summary(self):
        return f"{super().summary()} Interest rate: {self.interest_rate}"


"""Unit tests"""


class AccountTest(unittest.TestCase):
    def test_constructor(self):
        account = Account(1001, 0)
        self.assertEqual(account.account_number, 1001)
        self.assertEqual(account.balance, 0)

    def test_deposit(self):
        account = Account(1001, 0)
        account.deposit(7.50)
        self.assertEqual(account.balance, 7.50)

    def test_withdrawal(self):
        account = Account(1001, 100)
        account.withdraw(25)
        self.assertEqual(account.balance, 75)

    def test_get_balance(self):
        account = Account(1001, 100)
        account.withdraw(25)
        self.assertEqual(account.get_balance(), 75)

    def test_summary_string(self):
        account = Account(1, 100)
        account.deposit(24.51)
        self.assertEqual(account.summary(), "Account Number: 1 Balance: $124.51")


class SavingsAccountTest(unittest.TestCase):
    def test_constructor(self):
        account = SavingsAccount(1001, 0, 0.024)
        self.assertEqual(account.account_number, 1001)
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.interest_rate, 0.024)

    def test_interest_rate_set(self):
        account = SavingsAccount(1, 0, 0.024)
        self.assertEqual(account.interest_rate, 0.024)

    def test_apply_interest(self):
        account = SavingsAccount(1, 100, 0.24)
        account.apply_interest()
        self.assertEqual(account.balance, 102)

    def test_summary_string(self):
        account = SavingsAccount(1, 100, 0.24)
        account.apply_interest()
        self.assertEqual(
            account.summary(), "Account Number: 1 Balance: $102.0 Interest rate: 0.24"
        )


if __name__ == "__main__":
    # Perform unit tests
    unittest.main(verbosity=2)
