import unittest
from Accounts import create_account, close_account, account_list


class TestATMFunctions(unittest.TestCase):

    def test_create_account(self):
        create_account(54321, 98765477, "Savings", 1000.0)
        self.assertTrue(any(acct.account_number == 98765477 for acct in account_list))

    def test_create_account_2(self):
        create_account(61573, 20368415, "Savings", 0.0)
        self.assertTrue(any(acct.account_number == 20368415 for acct in account_list))

    def test_close_account(self):
        create_account(54321, 15603896, "Checking", 200.0)
        close_account(54321, 15603896)
        self.assertFalse(any(acct.account_number == 15603896 for acct in account_list))

    def test_close_account_2(self):
        create_account(61573, 15603896, "Checking", 0.0)
        close_account(61573, 15603896)
        self.assertFalse(any(acct.account_number == 15603896 for acct in account_list))

if __name__ == "__main__":
    unittest.main()
