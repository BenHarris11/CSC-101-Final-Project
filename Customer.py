class Customer:
    def __init__(self, name: str, customer_id: int, cust_accounts: {Account}):
        self.name = name
        self.customer_id = customer_id
        self.cust_accounts = cust_accounts  # Dictionary of Account objects
    def __repr__(self)-> str:
        return ('Customer: (Name: {}, Customer Id: {}, Accounts: {}'
                .format(self.name, self.customer_id, self.cust_accounts))

# The Master list of all customer objects within our system
customer_list = [
    Customer('Ethan Caldwell', 27489, [83746291, 15928347]),
    Customer('Sophia Bennett', 83924, [15384059, 76380555]),
    Customer('Lucas Montgomery', 61573, [38506911, 45846315]),
    Customer('Ava Whitaker', 48219, [82410599, 54820697]),
    Customer('Mason Everett', 92756, [48015974, 25840443]),
    Customer('Isabela Harrington', 35082, [73158920, 46255841]),
    Customer('Caleb Sinclair', 76820, [21036820, 75163028]),
    Customer('Olivia Mercer', 19468, [38492067, 48520614]),
    Customer('Nathaniel Holloway', 63913, [80635129, 14320685]),
    Customer('Emily Prescott', 80637, [24857447, 36921058]),
]
