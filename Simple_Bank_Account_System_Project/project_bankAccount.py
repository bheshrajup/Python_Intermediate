# -------------Simple Bank Account System------------

class BankAccount:

    # balance =0
    def __init__(self, balance, accountHolder):
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self, amount):
        # adding money to the bank account
        if (amount > 0):  # avoid negative amount value
            self.balance += amount
            print(
                f"Dear {self.accountHolder}, Rs.{amount} deposited. New balance is Rs.{self.balance}")
        else:
            print("Deposit amount must be positive ..")

    def withdraw(self, amount):
        # withdraw money from bank account
        if self.balance >= amount > 0:
            self.balance -= amount
            print(
                f"Rs.{amount} is deducted from your account. New balance is Rs.{self.balance}")

        else:
            print("Insufficient balance or invalid amount entered ..")

    def check_Balance(self):
        # show the current balanace of the bank account
        print(f"Account holder: {self.accountHolder}")
        print(f"Current balance: {self.balance}")


myAccount = BankAccount(0, "Bheshraj Upadhyaya")
myAccount.deposit(2000)
# myAccount.deposit(-1000)  # validated
myAccount.withdraw(500)
# myAccount.withdraw(-1000) # validated
myAccount.check_Balance()
myAccount.deposit(2000)
myAccount.check_Balance()

