import unittest
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	
from excel_add_mark import add_mark_in_table
from config import SPREAD_SHEET_ID
from config import CREDENTIALS_FILE
import logging
import logging.config

logging.config.fileConfig('logging_config.conf')
logger = logging.getLogger(__name__)

class AddMarkTest(unittest.TestCase):

    def test_add_mark(self):
        try:
            logger.info('Got into the test_add_mark method')
            add_mark_in_table('18-ISbo-2a', D10, 1)

            credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
            httpAuth = credentials.authorize(httplib2.Http())
            service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

            range = '18-ISbo-2a!D10'

            request = service.spreadsheets().values().get(spreadsheetId = SPREAD_SHEET_ID, ranges = range)
            
            self.assertEqual(reques.values(), 1)
            logger.info('The test_add_mark method has completed its execution')
        except Exception as ex:
            logger.exception(ex)




