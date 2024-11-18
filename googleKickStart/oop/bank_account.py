import random
class Account:
    def __init__(self, name, deposit):
        self.name = name
        self.number = random.randint(10000, 99999)  # needs to be unique number not random only
        self.balance = deposit
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def display_available_balance(self):
        print(f"Your available balance is: {self.balance} EGP")

accounts = []
main_menu = True

while main_menu:
    print("""
        Enter 1 to create a new account
        Enter 2 to access your existing account
        Enter any other character to exit 
    """)
    choice = input()
    match choice:
        case '1':
            new_account = True
            name = input("Enter your name: ")
            deposit = int(input("Enter your initial deposit: "))
            while deposit is not int or deposit < 100:  # needs testing
                deposit = int(input("Please, enter a positive number not less than 100 EGP: "))
            for acc in accounts:
                if acc.name == name:
                    new_account = False
                    print(f"""
                        Hey, {acc.name}
                        Account is already existing with number: {acc.number}
                    """)
            if new_account:
                account = Account(name, deposit)
                accounts.append(account)
                print(f"""
                    Hey, {account.name}
                    Your account number is: {account.number}
                    Your current balance is: {account.balance} EGP
                """)
        case '2':
            account_menu = True
            existing_account = False
            account_index = 0
            name = input("Enter your name: ")
            number = int(input("Enter your account number: "))
            for acc in accounts:
                if acc.name == name:
                    if acc.number == number:
                        existing_account = True
                        account_index = accounts.index(acc)
                        break
            if existing_account:
                while account_menu:
                    print("""
                        Enter 1 to withdraw from your account
                        Enter 2 to deposit to your account
                        Enter 3 to show your available balance
                        Enter 4 to return to Main Menu
                        Enter any other character to exit 
                    """)
                    choice = input()
                    match choice:
                        case '1':
                            withdraw_amount = int(input("Enter withdraw amount: "))
                            accounts[account_index].withdraw(withdraw_amount)
                            accounts[account_index].display_available_balance()
                        case '2':
                            deposit_amount = int(input("Enter deposit amount: "))
                            accounts[account_index].deposit(deposit_amount)
                            accounts[account_index].display_available_balance()
                        case '3':
                            accounts[account_index].display_available_balance()
                        case '4':
                            account_menu = False
                        case _:
                            account_menu = False
                            main_menu = False
            else:
                print("Account doesn't exist, or account number is incorrect!")
        case _:
            main_menu = False