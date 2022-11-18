from abc import ABC, abstractmethod

class Stationery(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, color):
        super().__init__(title = 'Ручка')
        self.color = "Синий"

    def draw(self):
        print("Ручка пишет")


class Pencil(Stationery):

    def draw(self):
        print("Карандаш пишет")



class Handle(Stationery):

    def draw(self):
        print("Маркер пишет")



pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")


print(pen.title, pen.color), pen.draw()
print(pencil.title), pencil.draw()
print(handle.title), handle.draw()
