alphabet = 'abcdefghijklmnopqrstuvwxyz'
gen = (i for i in alphabet)
d = {key : value for key, value in zip(range(1,24), gen)}
print(d)