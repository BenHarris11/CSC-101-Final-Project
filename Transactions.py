class Transaction:
    def __init__(self, transaction_type, amount, account_number, target_account=None):
        self.transaction_type = transaction_type  # "Deposit", "Withdrawal", "Transfer"
        self.amount = amount
        self.account_number = account_number
        self.target_account = target_account

    # Allows user to deposit money into their chosen account
    # input: A customer id and account number to specify which account is getting the money
    # input: An amount to be deposited
    # output: None, just prints a confirmation message
    def deposit(self, account, amount)-> None:
        """Deposits money into the account."""
        account.balance += amount
        print(f"Deposited ${amount} into account {account.account_number}. New balance: ${account.balance}")

    # Allows user to withdraw money from their chosen account
    # input: A customer id and account number to specify which account is being withdrawn from
    # input: An amount to be withdrawn
    # output: None, just prints a confirmation message or an error message if the amount is invalid
    def withdraw(self, account, amount):
        """Withdraws money if sufficient balance is available."""
        if amount <= account.balance:
            account.balance -= amount
            print(f"Withdrawn ${amount} from account {account.account_number}. New balance: ${account.balance}")
        else:
            print("Insufficient funds.")

    # Allows user to transfer money between their own accounts or between their account and
    # another customer's account
    # input: customer id and account number of account sending the money
    # input: customer id and account number of account receiving the money
    # output: None, just prints a confirmation message or error message if ther is one.
    def transfer(self, from_account, to_account, amount):
        """Transfers money to another account."""
        if amount <= from_account.balance:
            from_account.balance -= amount
            to_account.balance += amount
            print(f"Transferred ${amount} from account {from_account.account_number} to account {to_account.account_number}.")
        else:
            print("Insufficient funds.")
