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

# Creates a new Account object and appends it to our account_list
# inputs: All the attributes for a new Account object, with the same data types
# output: None, just appends the account_list
def create_account(customer_id: int, account_number: int, account_type: str, balance: float)-> None:
    account_list.append(Account(customer_id, account_number, account_type, balance))

# Removes an existing Account object from our account_list and returns an Error message
# if the account is not found
# inputs: the customer id & account number for the account to be deleted
# output: None, either updates the account_list or prints an error message
def close_account(customer_id: int, account_number: int)-> None:
    target = None
    for acct in account_list:
        if customer_id == acct.customer_id and account_number == acct.account_number:
            target = acct
    if target:
        account_list.remove(target)
    else:
        print("Account Not Found")