class Cat:

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        return "Мяу"

    def myr(self):
        return "Мур"

    def growl(self):
        return "Ррр"

pushistik = Cat("Пушистик","Рыжий",10)

print(pushistik.name, pushistik.color, pushistik.age)

print(pushistik.meow())
