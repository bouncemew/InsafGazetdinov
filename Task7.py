import re

class Time():

    @classmethod
    def from_string(cls, timestr='23:59:50'):
        time_re = re.compile('^(?:([01]?\d|2[0-3]):([0-5]?\d):)?([0-5]?\d)$')
        new_time = re.match(time_re, timestr)
        print(new_time.group())

t = Time()
t.from_string()

