class Batary():
    def __init__(self):
        self.capacity = []
        self.max_charge = 5

    def __str__(self):
        return '[' + ''.join(self.capacity) +']'

    def charge(self):
        if len(self.capacity) >= self.max_charge:
            print("Зарядка полная")
        else:
            self.capacity.append(')')

    def discharge(self):
        try:
            self.capacity.pop(0)
        except IndexError:
            print("Нет зарядки")

bat = Batary()
bat.charge()
bat.charge()
bat.charge()
bat.discharge()
bat.charge()
bat.charge()
bat.discharge()
bat.discharge()
print(bat)




