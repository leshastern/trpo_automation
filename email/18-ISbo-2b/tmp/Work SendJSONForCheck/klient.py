import socket
import global_Letter
import global_User
import global_LetterResult
import json
import select


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

        port1 = 10001
        port2 = 10002
        port3 = 10003
        port4 = 10005
        port5 = 10005

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

        student1 = global_User.User("Petya", "18-ISbo-2a", "petya@yandex.ru", True)
        student2 = global_User.User("Masha", "18-ISbo-2b", "masha@yandex.ru", True)
        student3 = global_User.User("Sanya", "18-ISbo-2a", "sanya@yandex.ru", True)
        student4 = global_User.User("Misha", "18-ISbo-2b", "misha@yandex.ru", True)
        student5 = global_User.User("Roma", "18-ISbo-2a", "Roma@yandex.ru", True)

        letter1 = global_Letter.Letter(student1, "Тело письма 1", "Содержание 1", 1, 1)
        letter2 = global_Letter.Letter(student2, "Тело письма 2", "Содержание 2", 2, 2)
        letter3 = global_Letter.Letter(student3, "Тело письма 3", "Содержание 3", 3, 3)
        letter4 = global_Letter.Letter(student4, "Тело письма 4", "Содержание 4", 4, 4)
        letter5 = global_Letter.Letter(student5, "Тело письма 5", "Содержание 5", 5, 5)

        letters = [letter1, letter2, letter3, letter4, letter5]

        for i in letters:
            sock = socket.socket()
            list = dataJSON.pop(0)
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
        for i in new_letters:
            print("Студент: ", i.Student)
            print("Тело письма: ", i.ThemeOfLetter)
            print("Вариант: ", i.VariantOfLab)
            print("Сдана работа? ", i.IsOK)
            print("Комментарий к работе: ", i.Comment)
            print("Номер лабораторной: ", i.NumberOfLab)
            print()
main()