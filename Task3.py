def robot_hello():
    lst = []
    name = input("Введите свое имя: ")
    if name in lst:
        print(name)
    else:
        lst.append(name)
        print(f'Привет, {name}! Рад знакомству!')
robot_hello()
