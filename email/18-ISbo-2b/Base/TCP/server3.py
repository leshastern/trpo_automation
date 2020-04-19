import socket
import json
from time import sleep

"""Настройка модуля сервера через файл config.txt"""
config = open("config3.txt", "r")
HOST = config.readline()
HOST = HOST.replace("\n", '')
PORT = int(config.readline())
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    print(' Подключен:', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        recvdata = data.decode()
        print("Полученные данные:")
        print(recvdata)
        json_otv1 = """
               {
                   "messageType": 2,
                   "grade": 0,
                   "comment": ""
               }
               """
        json_otv2 = """
               {
                   "messageType": 3,
                   "key": "",
                   "text": "",
                   "rejectCode": ""
               }
               """
        json_otv3 = """
               {
                   "messageType": 4,
                   "errorMessage": ""
               }
               """
        otvet = json.loads(json_otv3)
        otvet["errorMessage"] = "Текст системной ошибки"
        otv = json.dumps(otvet)

        print(otv.encode())
        """Закоментировано, так как демонстрирует ситуацию, когда какие то неполадки на порту"""
        conn.send(otv.encode())
    conn.close()