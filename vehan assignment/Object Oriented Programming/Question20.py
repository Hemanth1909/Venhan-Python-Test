class BankAccount:
    def __init__(self,  account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance  = balance

    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
            return "Amount deposited successfully"
        else:
            return "Please enter the valid amount"

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.balance):
            self.balance -= amount
            return True
        else:
            return False
        
    def get_balance(self):
        return f"Current balance in the account is {self.balance}"
bank1 = BankAccount("123456", "Hemanth", 0)


print(bank1.get_balance())
print(bank1.deposit(500))
print(bank1.get_balance())
print(bank1.withdraw(200))
print(bank1.get_balance())
    