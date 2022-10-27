alphabet = 'abcdefghijklmnopqrstuvwxyz'
def gen_alph():
    for char in alphabet:
        yield char
gen = gen_alph()
for i in gen:
    print(i)