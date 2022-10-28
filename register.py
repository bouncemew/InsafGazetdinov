log = input("Введите логин: ")
b = False
loglist = ["Insaf", "Ivan", "Sergey"]

def checker():
    b = False
    if log not in loglist:
        b = True
    return b


def validate():
    valid = ["#", "$", "%", "&"]
    if valid[0] in log:
        return
    elif valid[1] in log:
        return
    elif valid[2] in log:
        return
    elif valid[3] in log:
        return
    else:
        b = True
    return b


def register():
    if checker() == True and validate() == True:
        loglist.append(log)
        print("Вы прошли проверку и зарегистрировались")
    else:
        print("Вы не прошли проверку или вы зарегистрированы")
