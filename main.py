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
        return True if self.get_balance() >= amount else False

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

from collections import defaultdict
def create_spend_chart(categories: [Category]) -> None:
    # spent_by_category_value = [0] * len(categories)
    spent_by_category_value = defaultdict(int)
    for i, categorie in enumerate(categories):
        for ledger in categorie.ledger:
            amount = ledger['amount']
            if amount < 0:
                # spent_by_category_value[i] -= amount
                spent_by_category_value[categorie.name] -= amount

    print(spent_by_category_value)
    # get max
    sum_value = sum([v for v in spent_by_category_value.values()])
    print(sum_value)
    for key in spent_by_category_value:
        value = spent_by_category_value[key]
        spent_by_category_value[key] = round((value / sum_value) * 10) * 10
    print(spent_by_category_value)
    out = 'Percentage spent by category'

    for i in range(11):
        str_value = f'{str((10 - i) * 10)}|'
        out += f'\n{str_value:>4}'
    out += '\n    ' + '-' * 3 * len(categories) + '-'


    print(out)


# Percentage spent by category
# 100|
#  90|
#  80|
#  70|
#  60| o
#  50| o
#  40| o
#  30| o
#  20| o  o
#  10| o  o  o
#   0| o  o  o
#     ----------
#      F  C  A
#      o  l  u
#      o  o  t
#      d  t  o
#         h
#         i
#         n
#         g


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(13.4,"qaws")
print(food)

create_spend_chart([food , clothing])