from src.logger.logger import Observer


class ConsoleLogger(Observer):
    def update(self, message: str):
        print(message)
