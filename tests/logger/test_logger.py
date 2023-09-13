import unittest
from financial_transaction_project.src.logger import Logger, Observer

class MockObserver(Observer):
    def update(self, message):
        pass

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_attach_detach_observers(self):
        observer1 = MockObserver()
        observer2 = MockObserver()

        self.logger.attach(observer1)
        self.logger.attach(observer2)

        self.assertEqual(len(self.logger.observers), 2, "Falha ao anexar observadores.")

        self.logger.detach(observer1)
        self.assertEqual(len(self.logger.observers), 1, "Falha ao desanexar observador.")

if __name__ == '__main__':
    unittest.main()
