import unittest
import httplib2
import requests
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from config import SPREAD_SHEET_ID
from config import CREDENTIALS_FILE

class Test_google(unittest.TestCase):
    
    def test_add_mark(self):
        
        from google import add_mark_in_table

        add_mark_in_table('List1', 'A1', '1')

        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

        ranges = 'List1!A1'

        request = service.spreadsheets().values().get(spreadsheetId = SPREAD_SHEET_ID, range = ranges)
        response = request.execute();
        new_one = response['values'][0][0]
        self.assertEqual(new_one, '1')

    def test_cleaning_email(self):

        from google import cleaning_email

        email = cleaning_email('VOLODYA KOTLYAROV <httprequests.is.good@gmail.com>')
        self.assertEqual(email, 'httprequests.is.good@gmail.com')

    def test_name_surname(self):

        from google import name_surname

        not_a_email = name_surname('VOLODYA KOTLYAROV <httprequests.is.good@gmail.com>')
        self.assertEqual(not_a_email, 'VOLODYA KOTLYAROV ')






