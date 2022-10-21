def alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for el in alphabet:
        print(el, "-", i, end = ', ')
        i += 1
alphabet()
def dict_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    d = {}
    for el in alphabet:
        d[i] = el
        i += 1
    print(d)
dict_alphabet()

