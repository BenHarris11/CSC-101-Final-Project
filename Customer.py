class Customer:
    def __init__(self, name: str, customer_id: int, cust_accounts: {Account}):
        self.name = name
        self.customer_id = customer_id
        self.cust_accounts = cust_accounts  # Dictionary of Account objects
    def __repr__(self)-> str:
        return ('Customer: (Name: {}, Customer Id: {}, Accounts: {}'
                .format(self.name, self.customer_id, self.cust_accounts))

