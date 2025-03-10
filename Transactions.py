import Customer
import Accounts
import Recipts

#Author: Karsten Sarmiento
class Transaction:
    def __init__(self, cust: Customer.Customer, acct: Accounts.Account,
                 amount: float, transaction_type: str, target_account, rec_name):
        self.cust = cust
        self.acct = acct
        self.transaction_type = transaction_type  # "Deposit", "Withdrawal", "Local Transfer", or "Interpersonal Transfer"
        self.amount = amount
        self.target_account = target_account # Could either be an Account object if transaction type is Transfer,
                                             # or None if transaction type is deposit or withdrawal
        self.rec_name = rec_name             # Could either be the name of the recipient of a transfer, or None if
                                             # transaction type is not "Interpersonal Transfer"
    def __repr__(self)-> str:
        return ('Transaction: (Customer ID: {}, Account Number: {}, Type: {}, Amount: {}, Target Account: {}, Recipient Name: {})'
                .format(self.cust.customer_id, self.acct.account_number,
                        self.transaction_type, self.amount, self.target_account, self.rec_name))


#Author: Karsten Sarmiento
# Allows user to deposit money into their chosen account
# input: A Customer object
# user input: An account id to specify which account will get the money
# user input: An amount to be deposited
# output: None, just prints a receipt or an error message
def deposit(cust: Customer.Customer)-> None:
    acct_num = int(input("Enter your account number: "))    # Getting account number from user
    if acct_num in cust.cust_accounts:
        for i in Accounts.account_list:
            if i.account_number == acct_num:
                acct = i                                    # Assigning the account object for the deposit
                amount = float(input("Enter the amount you wish to deposit: "))     # Getting deposit amount from user
                if amount > 0:
                    acct.balance += amount
                    transaction = Transaction(cust, acct, amount, "Deposit", None, None)
                    Recipts.generate_receipt(transaction)
                else:
                    print("Error: Amount must be a positive number")
    else:
        print("Error: You do not have an account with that account number")

#Auhor: Karsten Sarmiento
# Allows user to withdraw money from their chosen account
# input: A Customer Object
# user input: An account id to specify which account will be withdrawn from
# user input: An amount to be withdrawn
# output: None, just prints a receipt or an error message
def withdraw(cust: Customer.Customer)-> None:
    acct_num = int(input("Enter your account number: "))    # Getting account number from user
    if acct_num in cust.cust_accounts:
        for i in Accounts.account_list:
            if i.account_number == acct_num:
                acct = i                                    # Assigning the account object for the withdrawal
                amount = float(input("Enter the amount you wish to withdraw: "))     # Getting withdrawal amount from user
                if 0 < amount < acct.balance:
                    acct.balance -= amount
                    transaction = Transaction(cust, acct, amount, "Withdrawal", None, None)
                    Recipts.generate_receipt(transaction)
                else:
                    print("Error: Invalid Amount")
    else:
        print("Error: You do not have an account with that account number")

#Author: Karsten Sarmiento
# Allows user to transfer money between two of their own accounts
# input: A Customer object
# user input: The account ID of the account that will send the money
# user input: The account ID of the account that will get the money
# user input: The amount to be transferred
# output: None, just prints a receipt or an error message.
def local_transfer(cust: Customer.Customer)-> None:
    send_acct_num = int(input("Enter the account number of your account from which you want to send the money: "))
    if send_acct_num in cust.cust_accounts:                     # Checks if user has the account they want to send from
        for i in Accounts.account_list:
            if i.account_number == send_acct_num:
                send_acct = i                                   # assigning the Account object that will send the money
                rec_acct_num = int(input("Enter the Account Number to receive the transfer: "))
                if rec_acct_num in cust.cust_accounts:          # Checks if user has the account they want to receive the money
                    for j in Accounts.account_list:
                        if j.account_number == rec_acct_num:
                            rec_acct = j                        # Assigning the Account object that will get the money
                            amount = float(input("Enter the amount you wish to withdraw: "))
                            if 0 < amount < send_acct.balance:
                                send_acct.balance -= amount
                                rec_acct.balance += amount
                                transaction = Transaction(
                                    cust, send_acct, amount, "Local Transfer", rec_acct, None)
                                Recipts.generate_receipt(transaction)
                            else:
                                print("Error: Invalid Amount")
                else:
                    print("Error: Receiving account could not be found")
    else:
        print("Error: You don't have an account with that account number")

#Author: Karsten Sarmiento
# Allows user to transfer money between their account and another customer's account
# input: A Customer object
# user input: The User's account ID that the money will be taken from
# user input: Recipient's Customer ID
# user input: The Recipient's account ID that will get the money
# user input: The amount to be transferred
# output: None, just prints a receipt or an error message.
def cust_to_cust_transfer(cust: Customer.Customer)-> None:
    send_acct_num = int(input("Enter the account number of your account from which you want to send the money: "))
    if send_acct_num in cust.cust_accounts:                     # Checks if user has the account they want to use
        for i in Accounts.account_list:
            if i.account_number == send_acct_num:
                send_acct = i                                   # assigning the Account object that will send the money
                rec_cust_id = int(input("Enter the Customer ID of recipient: "))
                all_cust_ids = [x.customer_id for x in Customer.customer_list]
                if rec_cust_id in all_cust_ids:                             # Checks if the recipient exists in our system
                    for j in Customer.customer_list:
                        if j.customer_id == rec_cust_id:
                            rec_cust = j                                    # Assigning the Customer object for the recipient
                            rec_acct_num = int(input("Enter the Account Number to receive the transfer: "))
                            if rec_acct_num in rec_cust.cust_accounts:      # Checks if the receiving account is owned by recipient
                                for k in Accounts.account_list:
                                    if k.account_number == rec_acct_num:
                                        rec_acct = k                        # Assigning the Account object that will get the money
                                        amount = float(input("Enter the amount you wish to withdraw: "))
                                        if 0 < amount < send_acct.balance:
                                            send_acct.balance -= amount
                                            rec_acct.balance += amount
                                            transaction = Transaction(cust, send_acct, amount,
                                                                      "Interpersonal Transfer", rec_acct, rec_cust.name)
                                            Recipts.generate_receipt(transaction)
                                        else:
                                            print("Error: Invalid Amount")
                            else:
                                print("Error: Receiving account could not be found")
                else:
                    print("Error: Customer could not be found")
    else:
        print("Error: You don't have an account with that account number")