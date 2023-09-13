import unittest

from src.logger.console_logger import ConsoleLogger

class TestConsoleLogger(unittest.TestCase):
    def setUp(self):
        self.console_logger = ConsoleLogger()

    def test_console_logger_update(self):
        message = "Test message"
        self.assertIsNone(self.console_logger.update(message), "A atualização do logger de console não funcionou corretamente.")

if __name__ == '__main__':
    unittest.main()
