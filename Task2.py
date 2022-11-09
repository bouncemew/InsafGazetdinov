import re

def check():
    try:
        class MyExeption(Exception):
            pass
        word = input("Введите слово: ")
        if re.search("[!@#$%^&*]", word, re.I) != None:
            raise MyExeption
        else:
            print(word)
    except MyExeption:
        print("В слове недопустимые символы")
check()

