import re

def find_log():
    lst = []
    with open('log.txt') as str_log:
        for line in str_log:
            ip = re.match('\w+.\w+.\w+.\w+', line)
            ip = ip.group(0)
            lst.append(ip)
    d = {x: lst.count(x) for x in lst}
    return max(d.values())
print(find_log())