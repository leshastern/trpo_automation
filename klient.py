import socket

sock = socket.socket()

def send_text(text):
    """Отправка данных в строковом представлении"""
    sock.send(text.encode())
    print("Данные отправлены")

def recv_text():
    """Получение данных в стоковом представлении"""
    text = sock.recv(1024)
    print("Данные получены:", text.decode())

def send_json(name_file):
    """Отправнение данных в формате JSON. На вход имя файла JSON"""

    file = open(name_file, "r")
    str_json = file.read()
    sock.send(str_json.encode())
    file.close()
    print("Данные JSON отправлены")

def recv_json(name_file):
    """Получение данных в формате JSON. На вход имя выходного файла"""
    obj = sock.recv(1024)
    file = open(name_file, "w")
    file.write(obj.decode())
    file.close()
    print("Данные получены и записаны в файл")

try:
    sock.connect(('192.168.0.106', 9090))

    """Проверка отправки и получения данных в текстовом формате"""
    send_text("Отправляю текст")
    recv_text()

    """Проверка отправки и получения данных в JSON формате"""
    send_json("read_file.json")
    recv_json("write_file.json")

finally:
    sock.close()
    print("Соединение разорвано")
