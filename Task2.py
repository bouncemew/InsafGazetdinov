class Good:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def calc(self):
        cost = self.price * self.weight
        return cost

apple = Good('apple', price = 100, weight = 1.5)

print(apple.name, apple.price, apple.weight, apple.calc())

pear = Good('pear', price = 120, weight = 0.8)

print(pear.name, pear.price, pear.weight, pear.calc())