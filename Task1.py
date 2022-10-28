from math import *
def engineer():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    root1 = sqrt(a)
    root2 = sqrt(b)
    power1 = pow(a,b)
    power2 = pow(b,a)
    return root1, root2, power1, power2
print(engineer())