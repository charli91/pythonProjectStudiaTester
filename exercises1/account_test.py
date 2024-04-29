from Account import Account
import unittest

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(3123.45, 'PL09184053349573708223772624')

    def test_1_account_deposit(self):
        self.assertEqual(self.account.deposit(492.79), 3616.24)

    def test_2_account_withdraw(self):
        self.assertEqual(self.account.withdraw(100), 3023.45)

    def test_3_account_withdraw_over_limit(self):
        with self.assertRaises(Exception):
            self.account.withdraw(3123.46)

    def test_4_get_balance(self):
        self.assertEqual(self.account.get_balance(), f'Balance: 3123.45 PLN, IBAN: PL09184053349573708223772624')


