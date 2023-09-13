import unittest
from unittest.mock import Mock
from typing import Dict
from src.entities.transaction import Transaction
from src.repositories.account_repository import AccountRepository
from src.logger.logger import Logger
from src.use_cases.transaction_use_case import TransactionUseCase

class TestTransactionUseCase(unittest.TestCase):
    def setUp(self):
        # Configura objetos mock para account_repository e logger
        self.account_repository = AccountRepository(initial_balances={1: 100.0, 2: 200.0})
        self.logger = Logger()
        self.logger.notify = Mock()

        # Cria uma instância de TransactionUseCase para testes
        self.transaction_use_case = TransactionUseCase(self.account_repository, self.logger)

    def test_validate_transaction_valid(self):
        # Testa a validação de uma transação válida
        transaction = Transaction(1, "09/09/2023 14:15:00", 1, 2, 50.0)
        result = self.transaction_use_case.validate_transaction(transaction)
        self.assertTrue(result)
        self.assertFalse(self.logger.notify.called)

    def test_execute_transaction_successful(self):
        # Testa a execução de uma transação bem-sucedida
        transaction = Transaction(1, "09/09/2023 14:15:00", 1, 2, 50.0)
        self.transaction_use_case.execute_transaction(transaction)
        self.assertTrue(self.logger.notify.called)

    def test_execute_transaction_insufficient_balance(self):
        # Testa a execução de uma transação com saldo insuficiente
        transaction = Transaction(1, "09/09/2023 14:15:00", 1, 2, 150.0)
        self.transaction_use_case.execute_transaction(transaction)
        self.assertTrue(self.logger.notify.called)

if __name__ == '__main__':
    unittest.main()
