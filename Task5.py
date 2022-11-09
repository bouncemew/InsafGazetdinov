from time import sleep

class trafficlight:

    def switch_red(self):
        self.red = sleep(1)
        print('Красный')

    def switch_green(self):
        self.green = sleep(2)
        print('Зелёный')

    def switch_yellow(self):
        self.yellow = sleep(0.5)
        print('Жёлтый')


tl = trafficlight()

tl.switch_red()
tl.switch_yellow()
tl.switch_green()



