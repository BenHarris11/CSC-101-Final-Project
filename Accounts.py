#Author: Karsten Sarmiento
class Account:
    def __init__(self, customer_id: int, account_number: int, account_type: str, balance: float):
        self.customer_id = customer_id
        self.account_number = account_number
        self.account_type = account_type  # e.g., "Checking", "Savings"
        self.balance = balance
    def __repr__(self)-> str:
        return ('Account: (Customer Id: {}, Account Num: {}, Account Type: {}, Balance: {})'
                .format(self.customer_id, self.account_number, self.account_type, self.balance))

#Author: Karsten Sarmiento
# The master list of all account objects within our system
account_list = [
    Account(27489, 15928347, "Savings", 6874.33),
    Account(83924, 15384059, "Checking", 1863.47),
    Account(83924, 76380555, "Savings", 8844.03),
    Account(61573, 45846315, "Savings", 45211.90),
    Account(92756, 48015974, "Checking", 452.43),
    Account(92756, 25840443, "Savings", 767.12),
    Account(76820, 21036820, "Checking", 3043.65),
    Account(76820, 75163028, "Savings", 19212.10),
    Account(19468, 38492067, "Checking", 123.78),
    Account(63913, 80635129, "Savings", 347.21),
    Account(63913, 14320685, "Savings", 4378.29),
    Account(80637, 36921058, "Checking", 15823.55),
]

#Author: Karsten Sarmiento
# Creates a new Account object and appends it to our account_list
# inputs: All the attributes for a new Account object, with the same data types
# output: None, just appends the account_list
def create_account(customer_id: int, account_number: int, account_type: str, balance: float)-> None:
    account_list.append(Account(customer_id, account_number, account_type, balance))

#Author: Karsten Sarmiento
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
        print("Account Successfully Closed")
    else:
        print("Account Not Found")