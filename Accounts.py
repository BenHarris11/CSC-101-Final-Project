class Account:
    def __init__(self, account_number, account_type, balance=0.0):
        self.account_number = account_number
        self.account_type = account_type  # e.g., "Checking", "Savings"
        self.balance = balance

    def create_account(self, account_number, account_type):
        """Creates a new bank account for the customer."""

    def close_account(self, account_number, account_type):
        """Closes a bank account for the customer."""