import socket
import global_LetterResult
import json
import select

new_letters = []
def SendJSONForCheck(jsonDates, letters):
    conf = open("config_port.json", "r")
    print(conf)
    config = conf.read()
    print(config)
    dataLab = json.loads(config)
    count = 0
    for i in letters:
        sock = socket.socket()
        letter = global_LetterResult.LetterResult()
        print(i.NumberOfLab)
        port = dataLab[str(i.NumberOfLab)]

        sock.connect(('192.168.0.106', port))
        print("Присоединен к", port)
        sock.send(jsonDates[count].encode())
        count += 1
        print("Данные отправлены..")
        """Ожидание ответа сервера 10 секунд"""
        ready = select.select([sock], [], [], 10)
        if ready[0]:
            otv_serv = sock.recv(1024)
            otvetServ = json.loads(otv_serv.decode())
            print("Пришел ответ с сервера: ", otv_serv)
            """Оценка лабораторной работы по ответу сервера"""
            if otvetServ["mark"] == "1":
                IsOk = True
            else:
                IsOk = False
            letter.Comment = otvetServ["comment"]
            letter.CodeStatus = 0
            letter.CodeStatusComment = ""
        else:
            sock.close()
            IsOk = False
            letter.CodeStatus = "06"
            letter.CodeStatusComment = "ERROR. Длительное ожидание ответа от сервера"
        letter.Student = i.Student
        letter.ThemeOfLetter = i.ThemeOfLetter
        letter.IsOK = IsOk
        letter.VariantOfLab = i.VariantOfLab
        letter.NumberOfLab = i.NumberOfLab
        letter.CodeStatusComment = ""
        """Добавление нового письма"""
        new_letters.append(letter)
        sock.close()