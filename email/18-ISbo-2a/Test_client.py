import unittest
import socket
import threading
import json
from config import PORTS
from client import send_a_laboratory_work_for_verification

class Test_client(unittest.TestCase):

    def test_1(self):

        #from Test_client import waiting_func

        number = '1'
        link = 'http://github.com'
        #server_thread = threading.Thread(target = waiting_func, args=(1, number, link, ), daemon=True)
        
        #server_thread.start()

        a = send_a_laboratory_work_for_verification(labNumber = number, labLink = link)

        self.assertEqual(a, 1)

    def test_2(self):
        
        number = '1'
        link = 'http://github.com'

        a = send_a_laboratory_work_for_verification(labNumber = number, labLink = link)

        self.assertIsNone(a)

    def test_3(self):

        #from Test_client import waiting_func
        
        number = '1'
        link = 'http://github.com'
        #server_thread = threading.Thread(target = waiting_func, args=(0, number, link, ), daemon=True)

        #server_thread.start()

        a = send_a_laboratory_work_for_verification(labNumber = number, labLink = link)

        self.assertEqual(a, 0)
        
if __name__ == '__main__':
    unittest.main()
