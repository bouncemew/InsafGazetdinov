entered_list = input("Введите 10 чисел через пробел ").split()
num_list = [int(i) for i in entered_list]
print(sum(num_list))