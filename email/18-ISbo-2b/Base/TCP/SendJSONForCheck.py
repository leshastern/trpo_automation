import socket

def SendJSONForCheck(JSONdates):
    try:
        while (len(JSONdates) != 0):
            sock = socket.socket()
            list = JSONdates.pop(0)
            json = list.pop(0)
            port = list.pop(0)
            sock.connect(('192.168.0.106', port))
            print("Присоединен к", port)
            sock.send(json.encode())
            print("Данные отправлены..")
            sock.close()
            print("Соединение", port, "разорвано")
    finally:
        print("Передача данных завершена")
