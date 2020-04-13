import socket
import global_LetterResult
import json
import select

def ProverkaJSON(numberLab, port):
    """Проверка. Правильный ли JSON пришёл и правильный ли порт к нему"""
    """Известен только порт для лаб. №3, поэтому здесь ещё будет настройка"""
    dataLab = {
        1: 10001,
        2: 10002,
        3: 10003,
        4: 10004,
        5: 10005,
        6: 10006,
        7: 10007,
        8: 10008,
        9: 10009,
        10: 10010,
        11: 10011,
        12: 10012,
        13: 10013,
    }
    flag = False
    print(dataLab[numberLab])
    print(port)
    if dataLab[numberLab] == port:
        flag = True
    return flag

new_letters = []
def SendJSONForCheck(JSONdates, letters):
    try:
        for i in letters:
            sock = socket.socket()
            list = JSONdates.pop(0)
            js = list.pop(0)
            port = list.pop(0)
            letter = global_LetterResult.LetterResult()
            """Проверка номера лабораторной работы и порта"""
            if ProverkaJSON(i.NumberOfLab, port):
                sock.connect(('192.168.0.106', port))
                print("Присоединен к", port)
                sock.send(js.encode())
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
            else:
                letter.Student = i.Student
                letter.ThemeOfLetter = i.ThemeOfLetter
                letter.IsOK = False
                letter.VariantOfLab = i.VariantOfLab
                letter.NumberOfLab = i.NumberOfLab
                """Код необходимо согласовать, взял пока свободный из таблицы"""
                letter.CodeStatus = "11"
                letter.CodeStatusComment = "ERROR. Не соответствие номер лабораторной и порта"
                """Добавление нового письма"""
                new_letters.append(letter)
            sock.close()
            print("Соединение", port, "разорвано")
            print()

    finally:
        print("End")