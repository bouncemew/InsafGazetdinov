import re

def log_dict():
    dct = {}
    lst = []
    with open('log.txt') as str_log:
        for line in str_log:
            line = line.replace('Mar', '3')
            ip = re.match('\w+.\w+.\w+.\w+', line)
            ip = ip.group(0)
            active = re.findall('GET|POST', line)
            active = ''.join(active)
            time = re.findall('\d{2}/\d{1}/\d{4}', line)
            time = ''.join(time)
            url = re.findall('/wp-login.php HTTP/1.1|/xmlrpc.php HTTP/1.1|/ HTTP/1.1', line)
            url = ''.join(url)
            lst.extend((active,time,url))
            dct[ip] = lst
            lst = []
    return dct
print(log_dict())