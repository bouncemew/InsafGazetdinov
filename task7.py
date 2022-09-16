str = "CamelCase"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = [str[0].lower()]
for char in str[1:]:
    if char in alphabet:
        res.append('_')
        res.append(char.lower())
    else:
        res.append(char)
res = ''.join(res)
print(res)