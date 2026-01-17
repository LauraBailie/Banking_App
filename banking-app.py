# Banking App
# Withdraw and Deposit
# Write to a text file once transaction is finished

# Bank class
class Bank:
    # deposit function
    def deposit(self, amount):
            try:
                amount = float(amount)
            except ValueError:
                amount = 0
            self.balance = self.balance + amount
            self.log(f"Deposited {amount}")
            
    # withdraw function
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance - amount
        self.log(f"Withdrew {amount}")
   
    # starting amount of 5.00
    def __init__(self, initial_amount=5.00):
        self.balance = initial_amount
      
    # writing transaction history to text file, appending every time  
    def log(self, trans_log):
        with open("transactions.txt", "a") as file:
            file.write(f"{trans_log}\t\t\tBalance: {self.balance}\n")
        
account = Bank(5.00)

# continuous loop until user decides to exit or presses ctrl+c
while True:
    try:
        action = input("Hello there! Would you like to deposit or withdraw today? ")
        action = str(action.lower())
    except KeyboardInterrupt:
        print("\nLeaving ATM\n")
        break
    
    # deposit or withdraw
    if action in ["deposit", "withdraw"]:
        if action == "deposit":
            amount = input("How much would you like to deposit? ")
            account.deposit(amount)
        else:
            amount = input("How much would you like to withdraw? ")
            account.withdraw(amount)
        print("Current balance:", account.balance)
    else:
        print("Invalid action. Please try again.")
            
    # continue?
    cont = input("Would you like to make another transaction? y/n ")
    if cont == "y":
        continue
    if cont == "n":
        print("\nThank you for banking with us, have a nice day!\n")
        break
        
            