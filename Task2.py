class Queque():
    def __init__(self):
        self.inside = ['Nastya', 'Nikita', 'Mariya']

    def __add__(self, other):
        self.inside.append(other)

    def __sub__(self, other):
        self.inside.pop(other)

    def __iadd__(self, other):
        self.inside.append(other)
        return self

    def __isub__ (self, other):
        self.inside.pop(other)
        return self

    def __str__(self):
        return "<=".join(self.inside)

    def add(self):
        name = input("Введите имя: ")
        self.inside.append(name)

    def take_out(self):
        self.inside.pop(0)

def input_name():
    name = input("Введите имя: ")
    return name

queque = Queque()
queque.add()
queque.take_out()
queque + input_name() # __add__
queque - 0 #__sub__
queque += input_name() #__iadd__
queque -= 0 #__isub__
print(queque)