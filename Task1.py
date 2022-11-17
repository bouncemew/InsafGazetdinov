from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass


class Dog(Animal):

    def say(self):
        print("Woof")


class Cat(Animal):

    def say(self):
        print("Meow!")


pushistik = Cat("white", "pushistic", 5)
print(pushistik.color, pushistik.name, pushistik.age)
pushistik.say()


sharik = Dog("black", "sharik", 10)
print(sharik.color, sharik.name, sharik.age)
sharik.say()