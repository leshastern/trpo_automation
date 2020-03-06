
import socket
import json
import random

class Server:

    #def server_otvet():
    
        sock = socket.socket()
        sock.bind(('', 12222))
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

        conn.close()      
        
            

    
    



