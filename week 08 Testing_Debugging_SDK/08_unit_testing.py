#!/usr/bin/env python3

"""
Modify the accounts.py program from the section on Classes and Objects
by adding unit tests for the Account and SavingsAccount classes.
Verify the following:
 - The constructor for each class assigns all values correctly
 - Functions return the proper values or modify other member variables
   appropriately
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
        self.balance += round((self.balance * self.interest_rate) / 12, 2)

    def summary(self):
        return f"{super().summary()} Interest rate: {self.interest_rate}"


class TestAccount(unittest.TestCase):
    def test_constructor(self):
        account = Account(account_number=2002, balance=5)
        self.assertEqual(account.account_number, 2002)
        self.assertEqual(account.balance, 5)

    def test_deposit(self):
        account = Account(account_number=2003, balance=15)
        account.deposit(100)
        self.assertEqual(account.balance, 115)

    def test_withdraw(self):
        account = Account(2008, 150)
        account.withdraw(100)
        self.assertEqual(account.balance, 50)

    def test_get_balance(self):
        account = Account(2020, 150)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 50)

    def test_summary_string(self):
        account = Account(2021, 500)
        account.withdraw(100)
        self.assertEqual(
            account.summary(),
            f"Account Number: 2021 Balance: $400",
        )


class TestSavingsAccount(unittest.TestCase):
    def test_constructor(self):
        account = SavingsAccount(2022, 5000, 0.0375)
        self.assertEqual(account.account_number, 2022)
        self.assertEqual(account.balance, 5000)
        self.assertEqual(account.interest_rate, 0.0375)

    def test_apply_interest(self):
        account = SavingsAccount(2012, 5000, 0.05)
        account.apply_interest()
        self.assertEqual(account.balance, 5020.83)

    def test_summary(self):
        account = SavingsAccount(2023, 5000, 0.05)
        self.assertEqual(
            account.summary(),
            f"Account Number: 2023 Balance: $5000 Interest rate: 0.05",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
