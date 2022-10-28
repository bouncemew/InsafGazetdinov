def get_password():
    pas = input("Введите пароль: ")
    h = hash(pas)
    return h
print(get_password())