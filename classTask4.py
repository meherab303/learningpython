

class BankAccount:
    
    def __init__(self, account_holder, account_number, balance, account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Type: {self.account_type}, Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return

        self.balance += amount
       

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return

        if self.balance >= amount:
            self.balance -= amount
           
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance

    


account1 = BankAccount("Alice Smith", "123456789", 5000.00, "Checking")

print(account1)


account1.deposit(2000.00)


account1.withdraw(1000.00)

print("\nCurrent Balance:", account1.get_balance())




