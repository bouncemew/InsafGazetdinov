from time import sleep

class trafficlight:

    def switch_lights(self):
        self.red = sleep(1)
        print('Красный')
        self.yellow = sleep(0.5)
        print('Жёлтый')
        self.green = sleep(2)
        print('Зелёный')


tl = trafficlight()
tl.switch_lights()
