alfa = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЄЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЄЮЯ0123456789'
kliucz = 1
#lang = input("Choose your language us or ua: ")
while True:
    message = input("Word for encryption: ").upper()
    result = ''
    for i in message:
        place = alfa.find(i)
        new_place = place + kliucz
        if i in alfa:
         result += alfa[new_place]
        else:
         result += i
    print(result)