def calculator():
    a = int(input("Введите первое число: "))
    oper = input("Введите операцию: ")
    b = int(input("Введите второе число: "))
    if oper == "/" and b == 0:
        print("Делить на 0 нельзя")
    else:
        print(eval(f'{a}{oper}{b}'))
calculator()