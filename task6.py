def caesars_cipher(text,key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for i in text:
        place = alphabet.find(i)
        new_place = place + key
        if i in alphabet:
            res += alphabet[new_place]
        else:
            res += i
    print(res)
caesars_cipher("ABC",3)
