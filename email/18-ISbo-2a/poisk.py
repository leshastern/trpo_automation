import pickle
import re;
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from apiclient import discovery
email='[Surname Name <email@gmail.com>]'
group='18-ИСбо-2а'
laba='8'
surname='ФИО'
def search_tablic(group,laba, surname):
    group1='(ТРПО) '+group
    a=email
    c=2
    CREDENTIALS_FILE = 'json файл'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',  'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
    spreadsheetId = 'ссылка на таблицу'
    range_name = group1+'!D2:D1000'
    table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
    count=ord('J')+int(laba)-1
    nomer_stolbca=chr(count)
    io=table.get('values')
    for name in io:
        if name[0]!=surname:
            c=c+1
        else:
            break
    position=str(nomer_stolbca)+str(c)
    return (group1,position)

