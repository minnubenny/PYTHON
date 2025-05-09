class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


#test example
account = BankAccount()     # Create a new bank account
account.deposit(100)        # Add 
account.withdraw(40)        # Withdraw
print(account.get_balance())  # Check and print current balance
