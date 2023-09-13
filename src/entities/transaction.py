from datetime import datetime

from src.logger.logger import Logger

class Transaction:
    def __init__(self, correlation_id: int, date_time: str, source_account: int, destination_account: int, amount: float):
        self.logger: Logger = Logger()

        
        if(correlation_id < 0):
             self.correlation_id = None
             self.log_error("Invalid correlation_id number. Cannot be less than zero.")
        else:
            self.correlation_id = correlation_id

        # Verifica se a data está no formato correto
        try:
            self.date_time = datetime.strptime(date_time, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            self.date_time = None
            self.log_error(f"Invalid date format: {date_time}")

        # Verifica se os IDs das contas são positivos
        if source_account <= 0 or destination_account <= 0:
            self.log_error("Invalid account numbers")
            self.source_account = None
            self.destination_account = None
        else:
            self.source_account = source_account
            self.destination_account = destination_account

        # Verifica se o valor da transação é válido
        if not isinstance(amount, (int,float)):
            self.log_error("Invalid transaction amount")
            self.amount = None
        elif amount < 0:
            self.log_error("Invalid transaction amount")
            self.amount = None
        else:
            self.amount = round(amount, 2)

    def log_error(self, message: str):
        # Registra mensagens de erro no log, se necessário
        #if self.correlation_id is not None:
        self.logger.notify(f"Transaction ID {self.correlation_id} error: {message}")

    def __str__(self):
        return f"Transaction ID: {self.correlation_id}, Amount: {self.amount}"
