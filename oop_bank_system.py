class BankAccount:
    def __init__(self , account_holder , balance ):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        print(f"The new balance is {self.balance}")
        self.transaction_history.append(f"Deposited : {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw : {amount}")

    def check_balance(self):
        print(f"The remaining balance is {self.balance}")

# Added a new feature show_history 
    def show_history(self):
        for show_history in self.transaction_history:
            print(show_history)

# Here we are creating a new object

a = BankAccount("Kumar", 2000)
a.deposit(500)
a.withdraw(200)
# Created a new object 
a.show_history()
a.check_balance()

