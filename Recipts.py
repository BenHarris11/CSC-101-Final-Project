def generate_receipt(t) -> None:
    from transactions_module import Transaction  # ✅ Import inside function

    if not isinstance(t, Transaction):
        raise TypeError("Expected a Transaction object")

    if t.transaction_type == "Deposit":
        print("Transaction Receipt:")
        print("{}, You just made a deposit into your {} account."
              .format(t.cust.name, t.acct.account_type))
        print("Account Number: {}".format(str(t.acct.account_number)))
        print("Deposit Amount: {}".format(str(t.amount)))
    elif t.transaction_type == "Withdrawal":
        print("Transaction Receipt:")
        print("{}, You just made a withdrawal from your {} account."
              .format(t.cust.name, t.acct.account_type))
        print("Account Number: {}".format(str(t.acct.account_number)))
        print("Amount Withdrawn: {}".format(str(t.amount)))
    elif t.transaction_type == "Local Transfer":
        print("Transaction Receipt:")
        print("{}, You just made a transfer from your {} account"
              .format(t.cust.name, t.acct.account_type))
        print("to your {} account.".format(t.target_account.account_type))
        print("Sending Account Number: {}".format(t.acct.account_number))
        print("Receiving Account Number: {}".format(t.target_account.account_number))
        print("Amount Transferred: {}".format(t.amount))
    else:
        print("Transaction Receipt:")
        print("{}, You just made a transfer from your {} account"
              .format(t.cust.name, t.acct.account_type))
        print("to an account owned by {}.".format(t.rec_name))
        print("Sending Account Number: {}".format(t.acct.account_number))
        print("Receiving Account Number: {}".format(t.target_account))
        print("Amount Transferred: {}".format(t.amount))
