from typing import Dict
from src.entities.transaction import Transaction
from src.repositories.account_repository import AccountRepository
from src.logger.logger import Logger
from src.use_cases.transaction_use_case import TransactionUseCase
from src.logger.console_logger import ConsoleLogger

def main():

    initial_balances: Dict = {
            938485762: 180,
            347586970: 1200,
            2147483649: 0,
            675869708: 4900,
            238596054: 478,
            573659065: 787,
            210385733: 10,
            674038564: 400,
            563856300: 1200
            # Inicialize outros saldos aqui
        }
    
    account_repository = AccountRepository(initial_balances)
    
    logger = Logger()
    console_logger = ConsoleLogger()
    logger.attach(console_logger)

    # Inicialize o caso de uso de transação
    transaction_use_case = TransactionUseCase(account_repository, logger)

    
    print("\n**Errors in transaction instantiation**\n")

    # Execute as transações (exemplo de transações)
    transactions = [
        Transaction(1, "09/09/2023 14:15:00", 938485762, 2147483649, 150),
        Transaction(2, "09/09/2023 14:15:05", 2147483649, 210385733, 149),
        Transaction(3, "09/09/2023 14:15:29", 347586970, 238596054, 1100),
        Transaction(4, "09/09/2023 14:17:00", 675869708, 210385733, 5300),
        Transaction(5, "09/09/2023 14:18:00", 238596054, 674038564, 1489),
        Transaction(6, "09/09/2023 14:18:20", 573659065, 563856300, 49),
        Transaction(7, "09/09/2023 14:19:00", 938485762, 2147483649, 44),
        Transaction(8, "09/09/2023 14:19:01", 573659065, 675869708, 150),
    ]

    print("\n**Transactions**\n")

    for transaction in transactions:
        transaction_use_case.execute_transaction(transaction)

    print("\n**Accounts and Balances**\n")
    
    # Exemplo: Recuperar todos os saldos após as transações
    all_account_ids = account_repository.get_all_account_ids()
    for account_id in all_account_ids:
        balance = account_repository.get_balance(account_id)
        print(f"Account: {account_id} | Balance: {balance:.2f}")

if __name__ == "__main__":
    main()
