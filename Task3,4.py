class Car:

    def __init__(self, color, brand, body, transmission, speed = 0):
        self.color = color
        self.brand = brand
        self.body = body
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print('speed = 10 km/h')
        self.speed = 10

    def stop(self):
        print('speed = 0 km/h')
        self.speed = 0

    def turn(self, t):
        print(f'Машина повернула {t}')

    def speed_up(self, i=1):
        print(f'speed = {self.speed + i} km/h')
        self.speed += i
        if self.body == 'truck' and self.speed > 60:
            print('Скорость превышена! Разрешенная скорость 60 км/ч')
        elif self.body == 'sedan' and self.speed > 80:
            print('Скорость превышена! Разрешенная скорость 80 км/ч')

    def speed_down(self, i=1):
        if self.speed == 0:
            print('speed = 0 km/h')
        else:
            print(f'speed = {self.speed - i} km/h')
            self.speed -= i
        if self.body == 'truck' and self.speed > 60:
            print('Скорость превышена! Разрешенная скорость 60 км/ч')
        elif self.body == 'sedan' and self.speed > 80:
            print('Скорость превышена! Разрешенная скорость 80 км/ч')

    def beep(self):
        print('Сигналит')

toyota = Car('white', 'toyota', 'sedan', 'automat')

print(toyota.color, toyota.brand, toyota.body, toyota.transmission)

toyota.beep()
toyota.turn('налево')

toyota.start()
toyota.speed_up(180)
toyota.speed_down(100)
toyota.stop()

print('\n')

mercedes = Car('black', 'mercedes', 'truck', 'mechanical')

print(mercedes.color, mercedes.brand, mercedes.body, mercedes.transmission)

mercedes.beep()
mercedes.turn('направо')

mercedes.start()
mercedes.speed_up(300)
mercedes.speed_down(80)
mercedes.stop()
