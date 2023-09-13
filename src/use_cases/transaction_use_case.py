from src.entities.transaction import Transaction
from src.logger.logger import Logger
from src.repositories.account_repository import AccountRepository


class TransactionUseCase:
    def __init__(self, account_repository: AccountRepository, logger: Logger):
        self.account_repository = account_repository
        self.logger = logger

    def validate_transaction(self, transaction: Transaction) -> bool:
        # Verifique se há campos nulos na transação
        if (
            transaction.correlation_id is None or
            transaction.date_time is None or
            transaction.source_account is None or
            transaction.destination_account is None or
            transaction.amount is None
        ):
            self.logger.notify(f"Transaction ID {transaction.correlation_id} canceled. There are fields that are not valid for the transaction.")
            return False
        else:
            return True
        
    def execute_transaction(self, transaction: Transaction):

        if (self.validate_transaction(transaction) is False): return

        # Verifique se as contas de origem e destino existem
        if (
            transaction.source_account not in self.account_repository.get_all_account_ids() or
            transaction.destination_account not in self.account_repository.get_all_account_ids()
        ):
            self.logger.notify(f"Transaction ID {transaction.correlation_id} canceled. Source or destination account does not exist.")
            return
        
        source_account_balance = self.account_repository.get_balance(transaction.source_account)
        destination_account_balance = self.account_repository.get_balance(transaction.destination_account)

        if source_account_balance >= transaction.amount:
            new_source_balance = source_account_balance - transaction.amount
            new_destination_balance = destination_account_balance + transaction.amount

            self.account_repository.update_balance(transaction.source_account, new_source_balance)
            self.account_repository.update_balance(transaction.destination_account, new_destination_balance)

            self.logger.notify(f"Transaction ID {transaction.correlation_id} processed successfully. New balances: Origin Account: {new_source_balance:.2f} | Destination Account: {new_destination_balance:.2f}")
        else:
            self.logger.notify(f"Transaction ID {transaction.correlation_id} canceled due to insufficient balance.")
