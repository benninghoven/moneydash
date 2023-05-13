class BankAccount:

    def __init__(self, id, name, nickname, balance):
        self.id = id
        self.name = name
        self.nickname = nickname
        self.balance = balance

    def __str__(self):
        return f"{self.nickname} {self.balance}"
