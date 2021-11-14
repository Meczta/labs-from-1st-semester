# -*- coding: utf-8 -*-
import socket
import cezar

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)

client.connect(
    ('192.168.0.110', 1321)
)

while True:
    data = client.recv(2048)  #receive, пишем какое количество данных хотим получить за один пакет

    print(data.decode('utf-8'))
    print('Выберите действие:\n1.Кодировать\n2.Не кодировать')
    a = input(':::')
    client.send(a.encode('utf-8'))
    while True:
        message = input("Word for encryption: ")
        result = ''
        if a == '1':
            message = message.upper()
            for i in message:
                place = cezar.alfa.find(i)
                new_place = place + cezar.kliucz
                if i in cezar.alfa:
                    result += cezar.alfa[new_place]
                else:
                    result += i
            print('Слово с кодировкой:', result)
            print(result)
            client.send(result.encode('utf-8'))
        elif a == '2':
            client.send(message.encode('utf-8'))
        else:
            print('Вы ввели недопустимое значение')
