class BankAccount:
    
    def __init__(self, balance=0):
        self.balance = balance
        print("Account Created")
        print("Opening Balance:", self.balance)

# Customer gives opening balance
acc1 = BankAccount(5000)

# Customer does not give opening balance
acc2 = BankAccount()