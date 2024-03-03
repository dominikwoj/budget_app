class Category:
    def __init__(self):
        self.ledger = []

    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})

def create_spend_chart(categories):
    pass
