import unittest
import httplib2
import requests
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from config import SPREAD_SHEET_ID
from config import CREDENTIALS_FILE

class Test_google(unittest.TestCase):

    def test_add_mark(self):

        from APIgoogle import add_mark_in_table
        
        Decode.Decode_files(['Example.json'])        
        add_mark_in_table('List1', 'A1', '1')

        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
        Decode.Finish(['Example.json.bak'])
        
        ranges = 'List1!A1'

        request = service.spreadsheets().values().get(spreadsheetId = SPREAD_SHEET_ID, range = ranges)
        response = request.execute();
        new_one = response['values'][0][0]
        self.assertEqual(new_one, '1')

    def test_cleaning_email(self):

        from APIgoogle import cleaning_email

        email = cleaning_email('VOLODYA KOTLYAROV <httprequests.is.good@gmail.com>')
        self.assertEqual(email, 'httprequests.is.good@gmail.com')

    def test_name_surname(self):

        from APIgoogle import name_surname

        not_a_email = name_surname('VOLODYA KOTLYAROV <httprequests.is.good@gmail.com>')
        self.assertEqual(not_a_email, 'VOLODYA KOTLYAROV ')

    # def test_search_email(self):

        # from APIgoogle import search_email

    def test_get_service(self):

        from APIgoogle import get_service
        Decode.Decode_files(['Example.json'])        
        service = get_service();

        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
        Decode.Finish(['Example.json.bak'])

        service.spreadsheets().values().batchUpdate(spreadsheetId = SPREAD_SHEET_ID, body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": 'List1!A2',
                 "majorDimension": "ROWS",     
                 "values": [ ['2'] ]
                }
            ]
        }).execute()

        request = service.spreadsheets().values().get(spreadsheetId = SPREAD_SHEET_ID, range = 'List1!A2')
        response = request.execute();
        new_one = response['values'][0][0]
        self.assertEqual(new_one, '2')

    def test_get_message(self):

        from APIgoogle import get_message
        from APIgoogle import get_service
        Decode.Decode_files(['Example.json']) 
        service = get_service()
        message_info = get_message(service, 'sanyabl.atchtozah.inya@gmail.com')
        Decode.Finish(['Example.json.bak'])

        hello_student = "Здравствуйте, " + 'человек, который делает всё невовремя' + "!"
        signature = " С уважением, Бот"
        our_msg = ' В Вашей работе обнаружены ошибки: ' + '- неверно указан номер ЛР ' + 'Просьба исправить их и отправить письмо повторно.'
        body_of_msg = hello_student + our_msg + signature

        our_info = {
            'email_id':'sanyabl.atchtozah.inya@gmail.com',
            'head_of_msg':'Обнаружены ошибки в работе',
            'body_of_msg':body_of_msg
            }

        self.assertEqual(message_info, our_info)

    def test_error_in_word(self):

        from APIgoogle import error_in_work

        Errors_list=[]
        Errors_list.append('неверно указано название предмета')
        Errors_list.append('неверно указан номер ЛР')

        validation_dictionary={ 
            'Number':1,
            'URL': "someurl.what",
            'Errors': Errors_list
            }

        answer = '- неверно указано название предмета'+"\n"+'- неверно указан номер ЛР'+"\n"

        get_error = error_in_work(validation_dictionary)

        self.assertEqual(get_error, answer)

    def test_send_message(self):

        from APIgoogle import send_message
        from APIgoogle import get_service
        from APIgoogle import get_message
        Decode.Decode_files(['Example.json']) 

        service = get_service()

        user_id = 'sanyabl.atchtozah.inya@gmail.com'
        email_of_student = 'sanyabl.atchtozah.inya@gmail.com'
        name_of_student = 'человек, который делает всё невовремя'
        number_of_templates = 1;

        Errors_list=[]
        Errors_list.append('неверно указан номер ЛР')
        validation_dictionary={ 
            'Number':1,
            'URL': "someurl.what",
            'Errors': Errors_list
            }

        send_message(service, user_id, email_of_student, name_of_student, number_of_templates, validation_dictionary)
        message_info = get_message(service, 'sanyabl.atchtozah.inya@gmail.com')
        Decode.Finish(['Example.json.bak'])

        hello_student = "Здравствуйте, " + name_of_student + "!"
        signature = " С уважением, Бот"
        our_msg = ' В Вашей работе обнаружены ошибки: ' + '- неверно указан номер ЛР '+ 'Просьба исправить их и отправить письмо повторно.'
        body_of_msg = hello_student + our_msg + signature

        our_info = {
            'email_id':'sanyabl.atchtozah.inya@gmail.com',
            'head_of_msg':'Обнаружены ошибки в работе',
            'body_of_msg': body_of_msg
            }
        
        self.assertEqual(message_info, our_info)

if __name__ == '__main__':
    unittest.main()
