#Author: Ben Harris
class Customer:
    def __init__(self, name: str, customer_id: int, cust_accounts: [int]):
        self.name = name
        self.customer_id = customer_id
        self.cust_accounts = cust_accounts  # List of Account ID's
    def __repr__(self)-> str:
        return ('Customer: (Name: {}, Customer Id: {}, Accounts: {})'
                .format(self.name, self.customer_id, self.cust_accounts))

#Author: Karsten Sarmiento
# The Master list of all customer objects within our system
customer_list = [
    Customer('Ethan Caldwell', 27489, [15928347]),
    Customer('Sophia Bennett', 83924, [15384059, 76380555]),
    Customer('Lucas Montgomery', 61573, [45846315]),
    Customer('Ava Whitaker', 48219, []),
    Customer('Mason Everett', 92756, [48015974, 25840443]),
    Customer('Isabela Harrington', 35082, []),
    Customer('Caleb Sinclair', 76820, [21036820, 75163028]),
    Customer('Olivia Mercer', 19468, [38492067]),
    Customer('Nathaniel Holloway', 63913, [80635129, 14320685]),
    Customer('Emily Prescott', 80637, [36921058]),
]
