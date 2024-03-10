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

    def transfer(self, amount: float, category_obj) -> None:
        if self.check_funds(amount) == True:
            self.withdraw(amount, f'Transfer to {category_obj.name}')
            category_obj.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def __str__(self) -> None:
        out = f'{self.name:*^30}'
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = item['description'][:(30 - (len(amount) + 1))]
            out += f"\n{description}{amount:>{30 - len(description)}}"
        out += f'\nTotal: {self.get_balance()}'
        return out


from collections import defaultdict


def create_spend_chart(categories: [Category]) -> None:
    # spent_by_category_value = [0] * len(categories)
    spent_by_category_value = defaultdict(int)
    for categorie in categories:
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
        print(f'value:{value}')
        # spent_by_category_value[key] = round((value / sum_value) * 10) * 10
        spent_by_category_value[key] = int((value / sum_value) * 10) * 10
    print(spent_by_category_value)
    out = 'Percentage spent by category'

    # values
    for i in range(100, -10, -10):
        str_value = f'{str(i)}|'
        out += f'\n{str_value:>4}'
        for sv in spent_by_category_value.values():
            out += ' o ' if i <= sv else ' ' * 3
        out += ' '

    # line: -------
    out += '\n    ' + '-' * 3 * len(categories) + '-\n'

    # categories name
    for i in range(max(len(c.name) for c in categories)):
        out += '    '
        for j in range(len(categories)):
            name = categories[j].name[i] if i < len(categories[j].name) else ' '
            out += f' {name} '
        out += ' \n'

    return out[:-1]


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
clothing.withdraw(20.4, "qaws")
auto = Category("Auto")
auto.deposit(30, 'dep1')
auto.withdraw(10, 'myjnia')
print(food)
print(clothing)
print(auto)

food_ = Category("Food")
food_.deposit(100, 'dep1')
food_.withdraw(60, 'myjnia')

# print(create_spend_chart([food , clothing, auto]))

print(create_spend_chart([food_, clothing, auto]))
print('next')
