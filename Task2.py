from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, parametr):
        self.parametr = parametr

    def __add__(self, other):
        return f'Общий расход ткани: {(self.parametr / 6.5 + 0.5)+(2 * other.parametr + 0.3)}'

    @abstractmethod
    def my_metod(self):
        pass


class Coat(Clothes):
    @property
    def expenses(self):
        return f'Расход ткани для пальто: {self.parametr / 6.5 + 0.5}'

    def my_metod(self):
        print("Я абстрактный класс")

class Costume(Clothes):
    @property
    def expenses(self):
        return f'Расход ткани для костюма: {2 * self.parametr + 0.3}'

    def my_metod(self):
        print("Я абстрактный класс")

coat = Coat(10)
costume = Costume(100)
print(coat + costume)
print(coat.expenses)
print(costume.expenses)
coat.my_metod()