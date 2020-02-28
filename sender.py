import socket
import json

class Sender:
     
    def SendURL(url, student, studentgroup, labnumber, port): 
        data = ({
            "Student": str(student),
            "StudyGroup": str(studentgroup),
            "LabNumber": str(labnumper),
            "LabLink": str(url)
        })
        jsn = json.dumps(data)
        sock = socket.socket()
        sock.bind(("127.0.0.1",port))
        sock.send(jsn)
        response = sock.recv(1024)
        while response:
            if (response["Answer"]==1):
                sock.close()
                return 1
            elif (response["Answer"]==0):
                sock.close
                return 0
            response = sock.recv(1024)

        sock.close()
        return 0