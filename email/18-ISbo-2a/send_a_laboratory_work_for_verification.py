import socket
import json

ports = {12000,12001,12002,12003,12004,12005,12006,12007,12008,12009} #Номера портов

##def SendURL(url, student, studentgroup, labnumber, port):
def send_a_laboratory_work_for_verification(labNumber, **kwargs): 
    """
    Метод, отправляющий работу на проверку
    labNumber - номер дабораторной работы
    **kwargs - все остальные параметры
    """
    if (labNumber != kwargs['labNumber']): return 0
    data = ({
        "labNumber": str(kwargs['labNumber']),
        "labLink": str(kwargs['labLink']),
    }) #Создание JSON
    jsn = json.dumps(data)
    sock = socket.socket() #Создание сокета
    sock.connect(("127.0.0.1",ports[labNumber-1])) #Подключение
    sock.send(jsn) #Отправка
    response = sock.recv(1024) #Получение ответа
    while response:
        if (response["Answer"]==1):
            sock.close()
            return 1
        elif (response["Answer"]==0):
            sock.close()
            return 0
        response = sock.recv(1024)

    sock.close()
    return 0
