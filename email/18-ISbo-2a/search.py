from datetime import datetime
from pprint import pprint
import httplib2
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
#email="Name Surname <1234@gmail.com>" ← пример email , который передает Саша
def cleaning_email(email):
 """
 Метод для выделения почты из передаваемой строки email.
 email - передаваемая строка с почтой
 Name Surname <1234@gmail.com> ← пример email который мне передают
 1234@gmail.com это будет запоминаться после метода очистки
 """
 comp = re.compile(r'<(\S*?)>')
 y=comp.search(email)
 q=y.group(0)
 z=q.replace('<','').replace('>','')
 return z
 def nameSurname(email):
 """
 Метод для выделения и передачи имени и фамилии.
 """
 comp = re.compile('(\S*?) '+'(\S*?) ')
 y=comp.search(email)
 q=y.group(0)
 return q
def Search_email(email):
  """
  Метод для поиска в таблице.
  email - передаваемая строка с почтой
  """
  a=email
  email=cleaning_email(email) # вызываю метод очистки строки в нужный формат
  CREDENTIALS_FILE = 'json файл'  #  ← имя скаченного файла с закрытым ключом
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',                                                                               'https://www.googleapis.com/auth/drive'])
  httpAuth = credentials.authorize(httplib2.Http())
  service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
  spreadsheetId = 'ссылка на таблицу'
  range_name = 'Лист1!B1:B1000'
  table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute() 
  # table- выводит нам словарь всех значение в ячейках B1:B1000
  result=re.search(email, str(table)) # поиск почты 
  if result != None:
   b=poisk(a)
  else:
   b=None
  return b

