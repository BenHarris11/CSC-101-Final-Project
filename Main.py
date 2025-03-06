from Accounts import Account, create_account, account_list
from Customer import Customer
from Transactions import Transaction

def main():
    """
    The main function for the banking system.

    This function provides a command-line interface for users to interact with the bank system.
    Users can log in to their accounts, perform transactions (deposit, withdraw, check balance), and log out.

    Arguments:
        None

    Returns:
        None
    """
    customers = {}
    while True:
        print("\nWelcome to the Bank System")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")


        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            account = next((acct for acct in account_list if acct.account_number == account_number), None)
            if account:
                print(f"Welcome, {account.account_type} Account Holder!")
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                    action = input("Choose an option: ")
                    if action == "1":
                        amount = float(input("Enter deposit amount: "))
                        transaction = Transaction("Deposit", amount, account_number)
                        transaction.deposit(amount)
                        account.balance += amount
                        print("Deposit successful! New Balance: $", account.balance)
                    elif action == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        if amount <= account.balance:
                            transaction = Transaction("Withdrawal", amount, account_number)
                            transaction.withdraw(amount)
                            account.balance -= amount
                            print("Withdrawal successful! New Balance: $", account.balance)
                        else:
                            print("Insufficient funds.")
                    elif action == "3":
                        print("Current Balance: $", account.balance)
                    elif action == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Account not found.")
        elif choice == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
