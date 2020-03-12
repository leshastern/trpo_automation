import socket
import json
from config import PORTS

##def SendURL(url, student, studentgroup, labnumber, port):
def send_a_laboratory_work_for_verification(labNumber, **kwargs): 
    """
    Метод, отправляющий работу на проверку
    labNumber - номер лабораторной работы
    **kwargs - все остальные параметры
    """
    if (labNumber != kwargs['labNumber']): return 0
    data = ({
        "labNumber": str(kwargs['labNumber']),
        "labLink": str(kwargs['labLink']),
    }) #Создание JSON
    jsn = json.dumps(data)
    sock = socket.socket() #Создание сокета
    sock.connect(("127.0.0.1",int(PORTS[str(kwargs['labNumber'])]))) #Подключение
    sock.send(jsn) #Отправка
    response = sock.recv(1024) #Получение ответа
    while response:
        if (response["labStatus"]==1):
            sock.close()
            return 1
        elif (response["labStatus"]==0):
            sock.close()
            return 0
        response = sock.recv(1024)

    sock.close()
    return 0
