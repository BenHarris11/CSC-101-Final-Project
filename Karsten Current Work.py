class Account:
    def __init__(self, customer_id: int, account_number: int, account_type: str, balance: float):
        self.customer_id = customer_id
        self.account_number = account_number
        self.account_type = account_type  # e.g., "Checking", "Savings"
        self.balance = balance
    def __repr__(self)-> str:
        return ('Account: (Customer Id: {}, Account Num: {}, Account Type: {}, Balance: {})'
                .format(self.customer_id, self.account_number, self.account_type, self.balance))

# The master list of all account objects within our system
account_list = []

def create_account(customer_id: int, account_number: int, account_type: str, balance: float)-> None:
    account_list.append(Account(customer_id, account_number, account_type, balance))

def close_account(customer_id: int, account_number: int):
    target = None
    for acct in account_list:
        if customer_id == acct.customer_id and account_number == acct.account_number:
            target = acct
    if target:
        account_list.remove(target)
    else:
        print("Account Not Found")


class Customer:
    def __init__(self, name: str, customer_id: int, cust_accounts: [int]):
        self.name = name
        self.customer_id = customer_id
        self.cust_accounts = cust_accounts  # List of Account ID's
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