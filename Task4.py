from Task3 import Box
from random import randint


box1 = Box(randint(100000, 999999), 'Omega', 'Moscow', 'Kazan')
print(box1.postcode, box1.name, box1.from_city, box1.target_city)
box2 = Box(randint(100000, 999999), 'IKEA', 'Sankt-Peterburg', 'Kazan')
print(box2.postcode, box2.name, box2.from_city, box2.target_city)
box3 = Box(randint(100000, 999999), 'Mega', 'Vladikavkaz', 'Kazan')
print(box3.postcode, box3.name, box3.from_city, box3.target_city)

class Track:

    def __init__(self, brand, color, transmission):
        self.color = color
        self.transmission = transmission
        self.brand = brand
        self.capacity = [box1, box2, box3]

    def __str__(self):
        return f'Грузовик: {self.brand}, Цвет: {self.color}, Коробка передач: {self.transmission} \nИтог загрузки и выгрузки: {self.capacity}'

    def __add__(self, other):
        self.capacity.append(other)

    def __sub__(self, other):
        self.capacity.remove(other)

box4 = Box(randint(100000, 999999), 'Megastroy', 'Moscow', 'Kazan')
toyota = Track('toyota', 'blue', 'mechanical')
toyota - box3
toyota + box4
print(toyota)



