def caesars_cipher(key):
    text = input("Введите шифруемый текст: ")
    text = text.upper()
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    res = ''
    for i in text:
        place = alphabet.find(i)
        new_place = place + key
        if i in alphabet:
            res += alphabet[new_place]
        else:
            res += i
    print(res)
caesars_cipher(3)