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

        jsonDates = []
        jsonDates.append(json1)
        jsonDates.append(json2)
        jsonDates.append(json3)
        jsonDates.append(json4)
        jsonDates.append(json5)

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


        conf = open("config_port.json", "r")
        config = conf.read()
        """Соответствие номера лабораторной и номера порта"""
        dataLab = json.loads(config)
        """Счётчик для параллельного обращения в два списка"""
        count = 0
        for i in letters:
            letter = global_LetterResult.LetterResult()

            """Данные для подключения"""
            sock = socket.socket()
            port = dataLab[str(i.NumberOfLab)]
            config = open("configServ.txt", "r")
            HOST = config.readline()
            HOST = HOST.replace("\n", '')
            if i.CodeStatus == "20":
                continue
            """Подключение и отправка JSON на порт"""
            sock.connect((HOST, port))
            sock.send(jsonDates[count].encode())
            count += 1
            IsOk = False
            """Ожидание ответа сервера 10 секунд"""
            ready = select.select([sock], [], [], 10)
            if ready[0]:
                otv_serv = sock.recv(1024)
                otvetServ = json.loads(otv_serv.decode())
                if otvetServ["messageType"] == 2:
                    if otvetServ["grade"] == 1:
                        IsOk = True
                    letter.Comment = otvetServ["comment"]
                    letter.CodeStatus = "30"
                    letter.Comment = ""
                elif otvetServ["messageType"] == 3:
                    letter.CodeStatus = "06"
                    letter.CodeStatusComment = ""
                    letter.Comment = otv_serv.decode()
                elif otvetServ["messageType"] == 4:
                    letter.CodeStatus = "07"
                    letter.CodeStatusComment = ""
                    letter.Comment = otv_serv.decode()
            else:
                sock.close()
                letter.CodeStatus = "06"
                letter.CodeStatusComment = "ERROR. Длительное ожидание ответа от сервера"
            """Заполнение полей letterResult"""
            letter.Student = i.Student
            letter.ThemeOfLetter = i.ThemeOfLetter
            letter.IsOK = IsOk
            letter.VariantOfLab = i.VariantOfLab
            letter.NumberOfLab = i.NumberOfLab
            """Добавление нового письма"""
            new_letters.append(letter)
            sock.close()

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