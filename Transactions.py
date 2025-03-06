class Transaction:
    def __init__(self, transaction_type, amount, account_number, target_account=None):
        self.transaction_type = transaction_type  # "Deposit", "Withdrawal", "Transfer"
        self.amount = amount
        self.account_number = account_number
        self.target_account = target_account

def deposit(self, account, amount):
        """Deposits money into the account."""
        account.balance += amount
        print(f"Deposited ${amount} into account {account.account_number}. New balance: ${account.balance}")

    def withdraw(self, account, amount):
        """Withdraws money if sufficient balance is available."""
        if amount <= account.balance:
            account.balance -= amount
            print(f"Withdrawn ${amount} from account {account.account_number}. New balance: ${account.balance}")
        else:
            print("Insufficient funds.")

    def transfer(self, from_account, to_account, amount):
        """Transfers money to another account."""
        if amount <= from_account.balance:
            from_account.balance -= amount
            to_account.balance += amount
            print(f"Transferred ${amount} from account {from_account.account_number} to account {to_account.account_number}.")
        else:
            print("Insufficient funds.")
