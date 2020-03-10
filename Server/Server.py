import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8080))
serversocket.listen(5)
print('Server is waiting for connections.')
while True:
    conn, addr = serversocket.accept()
    time.sleep(0.1)
    data = conn.recv(1024)
    print('Connection:', addr)
    print('------------------------------')
    print("Request Data from Browser")
    print('------------------------------')
    print(data)
    if not data:
        break
    conn.send(data)
    conn.close()
# Делаем задержку, чтобы цикл не сильно загружал процессор