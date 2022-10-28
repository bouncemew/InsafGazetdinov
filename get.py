def get_login():
    log = input("Введите логин: ")
    return log

def get_password():
    pas = input("Введите пароль: ")
    h = hash(pas)
    return h