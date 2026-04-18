# Bank Account

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.account_number}")
        else:
            print("You cannot deposit money")

    def withdraw(self, amount):
        if amount <=self.balance:
            self.balance -= amount
            print(f"Withdred {amount} to account {self.account_number}")
        else:
            print("Insufficient balance")

    def grt_balance(self):
        return self.balance


#Savings Account

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (1 + self.interest_rate)
        return interest

#Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
         if self.get_balance() - amount < self.minimum_balance:
             super().withdraw(amount)
         else:
            print("You cannot withdraw money: Minimum balance required")

print("Savings Account:")
sa = SavingsAccount(account_number=123, balance=10000, interest_rate=0.5)
sa.deposit(5000)
sa.withdraw(2000)
print("Balance:", sa.grt_balance())
print("Interest:", sa.calculate_interest())

print("Current Account:")
ca = CurrentAccount(account_number=123, balance=10000, minimum_balance=1000)
ca.deposit(5000)
ca.withdraw(2000)
print("Balance:", ca.grt_balance())
