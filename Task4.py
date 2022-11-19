class Deque():
    def __init__(self):
        self.lst = ['A','B','C', 'D']

    def __str__(self):
        return ','.join(self.lst)

    def enter_right(self):
        el = input('Введите элемент(справа): ')
        self.lst.append(el)

    def enter_left(self):
        el = input('Введите элемент(слева): ')
        self.lst.insert(0,el)

    def enter_center(self):
        el = input('Введите элемент(в центр): ')
        l = len(self.lst)/2
        l = int(l)
        self.lst.insert(l, el)

    def remove_right(self):
        self.lst.pop(-1)

    def remove_left(self):
        self.lst.pop(0)

    def remove_center(self):
        l = len(self.lst) / 2
        l = int(l)
        self.lst.pop(l)

deque = Deque()
deque.enter_left()
deque.enter_right()
deque.enter_center()
print(deque)
deque.remove_left()
deque.remove_right()
deque.remove_center()
print(deque)