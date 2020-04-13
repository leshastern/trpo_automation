import socket

def send_text(text, sock):
    """Отправка данных в строковом представлении"""
    sock.send(text.encode())
    print("Данные отправлены")

def recv_text(sock):
    """Получение данных в стоковом представлении"""
    text = sock.recv(1024)
    print("Данные получены:", text.decode())

def send_json(name_file, sock):
    """Отправнение данных в формате JSON. На вход имя файла JSON"""

    file = open(name_file, "r")
    str_json = file.read()
    sock.send(str_json.encode())
    file.close()
    print("Данные JSON отправлены")

def recv_json(name_file, sock):
    """Получение данных в формате JSON. На вход имя выходного файла"""
    obj = sock.recv(1024)
    file = open(name_file, "w")
    file.write(obj.decode())
    file.close()
    print("Данные получены и записаны в файл")

def main():
    try:
        file1 = open("student1.json", "r")
        json1 = file1.read()
        file2 = open("student2.json", "r")
        json2 = file2.read()
        file3 = open("student3.json", "r")
        json3 = file3.read()
        file4 = open("student4.json", "r")
        json4 = file4.read()
        file5 = open("student5.json", "r")
        json5 = file5.read()

        port1 = 9091
        port2 = 9092
        port3 = 9093
        port4 = 9094
        port5 = 9095

        list1 = [json1, port1]
        list2 = [json2, port2]
        list3 = [json3, port3]
        list4 = [json4, port4]
        list5 = [json5, port5]

        dataJSON = []
        dataJSON.append(list1)
        dataJSON.append(list2)
        dataJSON.append(list3)
        dataJSON.append(list4)
        dataJSON.append(list5)

        while (len(dataJSON) != 0):
            sock = socket.socket()
            list = dataJSON.pop(0)
            json = list.pop(0)
            port = list.pop(0)
            sock.connect(('192.168.0.106', port))
            print("Присоединен к", port)
            sock.send(json.encode())
            print("Данные отправлены..")
            sock.close()
            print("Соединение", port, "разорвано")
    finally:
        print("End")
main()