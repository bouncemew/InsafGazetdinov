def login():
    d = {}
    while True:
        log = input("Введите логин: ")
        password = input("Введите пароль: ")
        pas = d.get(log)
        if pas and pas == password:
            print("Вы успешно авторизовались")
        elif not pas:
            print("Регистрация прошла успешно")
            d[log] = password
            print(d)
        else:
            print("Доступ запрещён")
login()