import unittest
from datetime import datetime
from unittest.mock import MagicMock

from src.entities.transaction import Transaction
from src.logger.logger import Logger

class TestTransaction(unittest.TestCase):
    def setUp(self):
        # Configura um logger mock
        self.logger_mock = MagicMock(Logger())
        self.transaction = Transaction(1, "09/09/2023 14:15:00", 12345, 67890, 100.0)
        self.transaction.logger = self.logger_mock

    def test_valid_transaction(self):
        # Verifica se uma transação válida foi criada
        self.assertEqual(self.transaction.correlation_id, 1)
        self.assertIsInstance(self.transaction.date_time, datetime)
        self.assertEqual(self.transaction.source_account, 12345)
        self.assertEqual(self.transaction.destination_account, 67890)
        self.assertEqual(self.transaction.amount, 100.0)

    def test_invalid_correlation_id(self):
        # Testa com correlation_id negativo
        transaction = Transaction(-1, "09/09/2023 14:15:00", 12345, 67890, 100.0)
        self.assertIsNone(transaction.correlation_id)

    def test_invalid_date_format(self):
        # Testa com formato de data inválido
        transaction = Transaction(2, "09-09-2023 14:15:00", 12345, 67890, 100.0)
        self.assertIsNone(transaction.date_time)

    def test_invalid_account_numbers(self):
        # Testa com IDs de contas inválidos
        transaction = Transaction(3, "09/09/2023 14:15:00", -12345, 67890, 100.0)
        self.assertIsNone(transaction.source_account)
        self.assertIsNone(transaction.destination_account)

    def test_invalid_transaction_amount(self):
        # Testa com valor de transação inválido
        transaction = Transaction(4, "09/09/2023 14:15:00", 12345, 67890, -100.0)
        self.assertIsNone(transaction.amount)

if __name__ == '__main__':
    unittest.main()
