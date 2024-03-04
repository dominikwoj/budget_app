class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.ledger = []

    def deposit(self, amount: float, description: str) -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str) -> None:
        self.ledger.append({"amount": -amount, "description": description})

    def get_balance(self) -> float:
        return sum([i['amount'] for i in self.ledger])

    def transfer(self, amount:float, category_obj) -> None:
        self.withdraw(amount, f'Transfer to {category_obj.name}')
        category_obj.deposit(amount, f'Transfer from {self.name}')


def create_spend_chart(categories):
    pass


