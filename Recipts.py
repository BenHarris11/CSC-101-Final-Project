from Transactions import Transaction

class Receipt:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    # Creates a receipt based on the current transaction by the customer on the account
    # No input
    # Output: All information associated with transaction by customer
    def generate_receipt(self):
        """Generates a transaction receipt."""
