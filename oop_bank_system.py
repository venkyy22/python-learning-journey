class BankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"The new balance is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount

    def check_balance(self):
        print(f"The remaining balance is {self.balance}")

# Here we are creating a new object

a = BankAccount("Kumar", 2000)
a.deposit(500)
a.withdraw(200)
a.check_balance()
