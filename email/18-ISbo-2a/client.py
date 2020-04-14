import socket
import json
from config import PORTS
import log_method

##def SendURL(url, student, studentgroup, labnumber, port):
@log_method.log_method_info
def send_a_laboratory_work_for_verification(**kwargs): 
    """
    Метод, отправляющий работу на проверку
    **kwargs - все параметры Лабораторной работы
    """
    data = ({
        "labNumber": str(kwargs['labNumber']),
        "link": str(kwargs['labLink']),
        "code": 'null'
    }) #Создание JSON
    jsn = json.dumps(data)
    sock = socket.socket() #Создание сокета
    sock.connect(("127.0.0.1",int(PORTS[str(kwargs['labNumber'])]))) #Подключение
    log_method.logger.debug('send_a_laboratory_work_for_verification: Connect to 127.0.0.1:%s' % PORTS[str(kwargs['labNumber'])])
    sock.send(jsn) #Отправка
    log_method.logger.debug('send_a_laboratory_work_for_verification: Send file')
    response = sock.recv(1024) #Получение ответа
    log_method.logger.debug('send_a_laboratory_work_for_verification: Accepted the responce')
    while response:
        if (response["grade"]==True):
            sock.close()
            return response
        elif (response["grade"]==False):
            sock.close()
            return response
        response = sock.recv(1024)

    sock.close()
    return response
