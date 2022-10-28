from register import *
password = input("Введите пароль: ")
d = {"Insaf":"12345"}
def login():
    pas = d.get(log)
    if pas and pas == password:
        print("Доступ разрешён!")
    elif not pas:
        register()
        d[log] = password
        print("Регистрация прошла успешно")
    else:
        print("Доступ запрещён!")

def del_user():
    l = input("Напишите логин, который вы хотите удалить: ")
    d.pop(l)
    print("Логин удалён")
    return l


