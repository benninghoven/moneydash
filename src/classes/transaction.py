class Transaction:
    def __init__(self, id, account_id, amount, date, categories, name):
        self.id = id
        self.account_id = account_id
        self.amount = amount
        self.date = date
        self.categories = categories
        self.name = name
        self.card_nickname = ""

    def __str__(self):
        return f"{self.date} {self.card_nickname} {self.name} {self.amount}"
