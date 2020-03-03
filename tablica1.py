from datetime import datetime
from pprint import pprint
import httplib2
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
CREDENTIALS_FILE = 'наш json файл'  #  ← имя скаченного файла с закрытым ключом
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',                                                                               'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
spreadsheetId = 'ссылка на нашу таблицу'
range_name = 'Лист1!B:B100'
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
print(table)
#a='почта пользователя'
#if re.search(r'\bmilan070699@gmail.com\b', table):
 # print("Есть")
#else:
   #print("Нет")
