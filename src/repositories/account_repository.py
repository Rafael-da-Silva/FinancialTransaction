from typing import Dict

class AccountRepository:
    def __init__(self, initial_balances: Dict[int, float]):
        self.balances = initial_balances

    def get_balance(self, account_id: int) -> float:
        return self.balances.get(account_id, 0.0)

    def update_balance(self, account_id: int, new_balance: float) -> None:
        self.balances[account_id] = new_balance

    def get_all_account_ids(self):
        return list(self.balances.keys())
