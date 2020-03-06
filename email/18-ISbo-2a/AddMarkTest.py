import unittest
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	
from excel_add_mark import add_mark_in_table
from config import SPREAD_SHEET_ID
from config import CREDENTIALS_FILE

class AddMarkTest(unittest.TestCase):

    def test_add_mark(self):

        add_mark_in_table('18-ИСбо-2а', D10, 1)

        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

        range = '18-ИСбо-2а!D10'

        request = service.spreadsheets().values().get(spreadsheetId = SPREAD_SHEET_ID, range)
        
        self.assertEqual(reques.values(), 1)





