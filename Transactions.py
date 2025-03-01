class Transaction:
    def __init__(self, transaction_type, amount, account_number, target_account=None):
        self.transaction_type = transaction_type  # "Deposit", "Withdrawal", "Transfer"
        self.amount = amount
        self.account_number = account_number
        self.target_account = target_account

    def process_transaction(self):
        """Processes the transaction and updates accounts."""

    def deposit(self, amount):
        """Deposits money into the account."""


    def withdraw(self, amount):
        """Withdraws money if sufficient balance is available."""


    def transfer(self, target_account, amount):
        """Transfers money to another account."""