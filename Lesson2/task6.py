procent = int(input("Введите процент: "))
if procent % 10 == 1:
    print(procent, "процент")
elif procent % 10 >= 2 and procent % 10 <= 4:
    print(procent, "процента")
elif procent % 10 >= 5 and procent % 10 <= 9 or procent % 10 == 0:
    print(procent, "процентов")
