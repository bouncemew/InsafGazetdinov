import time

class Time():

    @classmethod
    def from_string(cls, timestr = '01:19:02'):
        cls.new_time = time.strptime(timestr, "%H:%M:%S")
        cls.new_time = time.strftime("%H:%M:%S", cls.new_time)
        print(cls.new_time)


t = Time()
t.from_string()