"""
Using the Account class example from the beginning of the Week 4 module, define a child class that represents a savings account.  Provide a means for calculating the interest in the savings account and applying the interest to the balance.  Add a summary method that prints the details of the account on one line.

Write a program that processes a small number of accounts in a loop, applies interest where applicable, and prints the account summary.

Hint:  You may need to use the isinstance() method to determine which class you are working with.
"""

#Account class with deposit, withdraw, get_balance and summary methods
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
        return f"Account Number: {self.account_number} Balance: ${round(self.balance, 2)}"
        

#SavingsAccount class inherits from the Account class and overrides the init method, with apply_interest and summary methods.
class SavingsAccount(Account):
    
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    
    def apply_interest(self):
        self.balance += (self.balance * self.interest_rate) / 12
        
    def summary(self):
        return f"{super().summary()} Interest rate: {self.interest_rate}"
    
#empty list called accounts
accounts = []

#create and add accounts to the list above
accounts.append(Account(1, 400.00))
accounts.append(Account(2, 500.00))
accounts.append(SavingsAccount(3, 350, .029))
accounts.append(SavingsAccount(4, 725, .029))

for account in accounts:
    #For every account in the list of accounts, we check if it is an instance of the SavingsAccount class
    if isinstance(account, SavingsAccount):
        #If it is a savingsAccount, only then we apply interest to the account
        account.apply_interest()
    #Print account summary
    print(account.summary())
