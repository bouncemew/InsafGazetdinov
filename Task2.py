class Father():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname




class Child(Father):

    def __init__(self, patronim):
        super().__init__('Kirill', 'Ivanov')
        self.patronim = patronim

kirill = Child('Maksimovich')
print(kirill.name, kirill.surname, kirill.patronim)
