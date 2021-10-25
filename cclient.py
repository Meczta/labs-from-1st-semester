import socket

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)

client.connect(
    ('26.145.225.176', 1234)
)

while True:
    data = client.recv(2048)  #receive, пишем какое количество данных хотим получить за один пакет

    print(data.decode('utf-8'))
    while True:
        client.send(input(':::').encode('utf-8'))