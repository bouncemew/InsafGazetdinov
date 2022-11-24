class Box:

    def __init__(self, postcode, name, from_city, target_city):
        self.__postcode = postcode
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    @property
    def postcode(self):
        return self.__postcode

    @property
    def name(self):
        return self.__name

    @property
    def from_city(self):
        return self.__from_city


    @property
    def target_city(self):
        return self.__target_city