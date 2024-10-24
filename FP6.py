class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}."
            else:
                return "Insufficient funds for this withdrawal."
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        return f"Current balance: ${self.balance:.2f}"

# Create an object here. The object should be an instance of the class
user_account_number = input("What is your account number? ")
user_account = BankAccount(user_account_number)

if user_account_number:
    print("Account verified!")
        
    while True:
        print("\nWhat would you like to do?")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
            
        user_choice = input("Enter the number of your choice: ")
            
        if user_choice == '1':
            # Call the check_balance function here
            print(user_account.check_balance())
        
        elif user_choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(user_account.deposit(amount))
        
        elif user_choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(user_account.withdraw(amount))
        
        elif user_choice == '4':
            print("Thank you for using the bank system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect account number. Please try again.")