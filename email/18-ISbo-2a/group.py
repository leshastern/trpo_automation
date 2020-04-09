import pickle
import re;
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from apiclient import discovery
def search_group(group,laba, surname):
    group1='(ТРПО) '+group
    c=1
    CREDENTIALS_FILE = 'json файл'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',  'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
    spreadsheetId = 'link'
    range_name = group1+'!G1:G1000'
    table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
    io=table.get('values')
    for name in io:
        if name[0]!=surname:
            c=c+1
        else:
            break
    nomer = group1+'!F'+str(c)+':'+'F'+str(c)
    table1 = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=nomer).execute()
    io1=table1.get('values')
    return io1[0][0]

