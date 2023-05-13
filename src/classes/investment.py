class Investment:

    def __init__(self, name, total_shares, total_value):
        self.name = name
        self.total_shares = total_shares
        self.total_value = total_value

    def __str__(self):
        return f"{self.name} {self.total_shares} shares worth ${self.total_value}"

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if not isinstance(other, Investment):
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self).__name__, type(other).__name__))
        new_total_shares = self.total_shares + other.total_shares
        new_total_value = self.total_value + other.total_value
        return Investment(self.name, new_total_shares, new_total_value)
