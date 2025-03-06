from Transactions import Transaction

class Receipt:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

#
    def generate_receipt(self):
        """Generates a transaction receipt."""
