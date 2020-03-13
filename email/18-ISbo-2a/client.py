import socket
import json
from config import PORTS
import logging
import logging.config

logging.config.fileConfig('logging_config.conf')
logger = logging.getLogger(__name__)

##def SendURL(url, student, studentgroup, labnumber, port):
def send_a_laboratory_work_for_verification(labNumber, **kwargs): 
    """
    Метод, отправляющий работу на проверку
    labNumber - номер лабораторной работы
    **kwargs - все остальные параметры
    """
    logger.info('Got into the send_a_laboratory_work_for_verification method')
    if (labNumber != kwargs['labNumber']): return 0
    data = ({
        "labNumber": str(kwargs['labNumber']),
        "labLink": str(kwargs['labLink']),
    }) #Создание JSON
    jsn = json.dumps(data)
    sock = socket.socket() #Создание сокета
    sock.connect(("127.0.0.1",int(PORTS[str(kwargs['labNumber'])]))) #Подключение
    logger.debug(f'Connect to 127.0.0.1:{int(PORTS[str(kwargs['labNumber'])])}')
    sock.send(jsn) #Отправка
    logger.debug('Send file')
    response = sock.recv(1024) #Получение ответа
    logger.debug('Accepted the responce')
    while response:
        if (response["labStatus"]==1):
            sock.close()
            logger.debug('Return - 1')
            logger.info('The send_a_laboratory_work_for_verification method has completed its execution')
            return 1
        elif (response["labStatus"]==0):
            sock.close()
            logger.debug('Return - 0')
            logger.info('The send_a_laboratory_work_for_verification method has completed its execution')
            return 0
        response = sock.recv(1024)

    sock.close()
    logger.info('The send_a_laboratory_work_for_verification method has completed its execution')
    return 0
