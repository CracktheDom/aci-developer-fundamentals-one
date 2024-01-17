class Account:
    account_num = 58475

    def __init__(self, balance=0):
        self.balance = balance
        self.account_num = account_num
        Account.account_num += 1

    def deposit(self, num):
        self.balance += num

    def withdraw(self, num):
        if self.balance - num < 0:
            print("Insufficient funds for withdrawal")
        else:
            self.balance -= num

    def display_balance(self):
        print(f"Available funds: ${self.balance:.2f}")
