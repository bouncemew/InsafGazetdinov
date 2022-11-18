from time import time, localtime

class Clock():

    @staticmethod
    def say_time():
        rez = localtime(time())
        print(f'{rez.tm_hour}:{rez.tm_min}:{rez.tm_sec}')


Clock.say_time()
