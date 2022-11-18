import re

class Time():

    @classmethod
    def from_string(cls, timestr='23:59:50'):
        cls.time_re = re.compile('^(?:([01]?\d|2[0-3]):([0-5]?\d):)?([0-5]?\d)$')
        cls.new_time = re.match(cls.time_re, timestr)
        print(cls.new_time.group())

t = Time()
t.from_string()

