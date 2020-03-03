from datetime import datetime
from pprint import pprint
import httplib2
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
class Tablica:
 def my_metod(a):
  CREDENTIALS_FILE = 'json файл'  #  ← имя скаченного файла с закрытым ключом
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',                                                                               'https://www.googleapis.com/auth/drive'])
  httpAuth = credentials.authorize(httplib2.Http())
  service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
  spreadsheetId = 'наша ссылка на таблицу'
  range_name = 'Лист1!B3:B1000'
  table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
  result=re.search(a, str(table))
  if result != None:
   b="Почта найдена"
  else:
   b="Почты нет в списке"
  return b


