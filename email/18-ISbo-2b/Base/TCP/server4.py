import socket

"""Настройка модуля сервера через файл config.txt"""
config= open("config4.txt", "r")
HOST=config.readline()
HOST= HOST.replace("\n", '')
PORT=int(config.readline())

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
print(' Подключен:', addr)

while True:
    data = conn.recv(1024)
    if not data: break
    recvdata = data.decode()
    print("Полученные данные:")
    print(recvdata)
conn.close()