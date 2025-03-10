from Accounts import Account, create_account, account_list
from Customer import Customer, customer_list
from transactions_module import deposit, withdraw

#Author: Ben Harris
def main():
    #The main function for the banking system.
    #Users can create an account, log in, perform transactions, and log out.

    while True:
        print("\nWelcome to the Bank System")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            customer_id = int(input("Enter a new Customer ID: "))
            account_number = int(input("Enter a new Account Number: "))
            account_type = input("Enter Account Type (Checking/Savings): ")
            balance = float(input("Enter initial deposit amount: "))

            new_customer = Customer(name, customer_id, [account_number])
            customer_list.append(new_customer)
            create_account(customer_id, account_number, account_type, balance)
            print("Account successfully created!")

        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            account = next((acct for acct in account_list if acct.account_number == account_number), None)
            customer = next((cust for cust in customer_list if account and cust.customer_id == account.customer_id),
                            None)

            if account and customer:
                print(f"Welcome, {customer.name}!")
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                    action = input("Choose an option: ")

                    if action == "1":
                        deposit(customer)
                    elif action == "2":
                        withdraw(customer)
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
