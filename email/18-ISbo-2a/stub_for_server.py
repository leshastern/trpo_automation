
import socket
import json
import random
import logging
import logging.config

logging.config.fileConfig('logging_config.conf')
logger = logging.getLogger(__name__)


def server_otvet(port):
   """
   Метод "заглушки" для сервера
   port - по какому порту будет настроено соединение
   (в дальнейшем, можно будет узнать номер лабораторной по номеру порта)
   """
   logger.info('Got into the server_otvet method')
   sock = socket.socket()
   sock.bind(('127.0.0.1', port))
   sock.listen(1)
   conn, addr = sock.accept()
   while True:
      data = conn.recv(1024)
      if not data:
         break
      r = random.randint(0, 1)
      data_j={
      "labStatus": r,
      }
      y = json.dumps(data_j)
      conn.send(y.encode())
      logger.debug(f'server_otvet send {r}')

   conn.close()     
   logger.info('The server_otvet method has completed its execution')
        
            

    
    



