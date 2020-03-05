from datetime import datetime
from pprint import pprint
import httplib2
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
#email="Name Surname <1234@gmail.com>" ← пример email , который передает Саша
def cleaning_email(email):
 comp = re.compile(r'<(\S*?)>')
 y=comp.search(email)
 q=y.group(0)
 z=q.replace('<','').replace('>','')
 return z
def Search_email(email):
  email=cleaning_email(email)
  CREDENTIALS_FILE = 'json файл'  #  ← имя скаченного файла с закрытым ключом
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',                                                                               'https://www.googleapis.com/auth/drive'])
  httpAuth = credentials.authorize(httplib2.Http())
  service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
  spreadsheetId = 'ссылка на таблицу'
  range_name = 'Лист1!B1:B1000'
  table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
  print(table)
  result=re.search(email, str(table))
  if result != None:
   b=1
  else:
   b=0
  return b

