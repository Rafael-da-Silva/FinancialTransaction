import unittest

from src.repositories.account_repository import AccountRepository

class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        # Configura um objeto AccountRepository com saldos iniciais
        initial_balances = {1: 100.0, 2: 200.0, 3: 300.0}
        self.account_repository = AccountRepository(initial_balances)

    def test_get_balance_existing_account(self):
        # Testa o método get_balance para uma conta existente
        balance = self.account_repository.get_balance(2)
        self.assertEqual(balance, 200.0)

    def test_get_balance_non_existing_account(self):
        # Testa o método get_balance para uma conta que não existe
        balance = self.account_repository.get_balance(4)
        self.assertEqual(balance, 0.0)

    def test_update_balance(self):
        # Testa o método update_balance para atualizar o saldo de uma conta
        self.account_repository.update_balance(1, 150.0)
        new_balance = self.account_repository.get_balance(1)
        self.assertEqual(new_balance, 150.0)

    def test_get_all_account_ids(self):
        # Testa o método get_all_account_ids para obter todos os IDs de conta
        account_ids = self.account_repository.get_all_account_ids()
        expected_ids = [1, 2, 3]
        self.assertEqual(account_ids, expected_ids)

if __name__ == '__main__':
    unittest.main()
