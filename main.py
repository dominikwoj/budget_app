class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.ledger = []

    def deposit(self, amount: float, description: str = '') -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = '') -> None:
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def check_funds(self, amount) -> bool:
        return True if self.get_balance() > amount else False

    def get_balance(self) -> float:
        return sum([i['amount'] for i in self.ledger])

    def transfer(self, amount:float, category_obj) -> None:
        if self.check_funds(amount) == True:
            self.withdraw(amount, f'Transfer to {category_obj.name}')
            category_obj.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def __str__(self) -> None:
        out = f'{self.name:*^30}'
        for item in self.ledger:
            amount = item['amount']
            description = item['description']
            out += f"\n{item['description'][:23]}{amount:>{30 - len(description) if len(description) < 23 else 23 }}"
        out += f'\nTotal: {self.get_balance()}'
        return out


def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)