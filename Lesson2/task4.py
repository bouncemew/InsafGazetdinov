first_num = int(input("Введите первое число: "))
operation = input("Введите операцию: ")
second_num = int(input("Введите второе число: "))
if operation == "+":
    result = first_num + second_num
    print("Ответ: ", result)
elif operation == "-":
    result = first_num - second_num
    print("Ответ: ", result)
elif operation == "/":
    if second_num == 0:
        print("Ошибка! На 0 делить нельзя")
    else:
        result = first_num / second_num
        print("Ответ: ", result)
elif operation == "*":
    result = first_num * second_num
    result = int(result)
    print("Ответ: ", result)
else:
    print("Вы неправильно ввели операцию")