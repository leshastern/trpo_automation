# coding: utf-8
import logging
import logging.config

logging.config.fileConfig('logging_config.conf')
logger = logging.getLogger(__name__)

def AddMarkInTable(table, cell, mark):
    import httplib2 
    import apiclient.discovery
    from oauth2client.service_account import ServiceAccountCredentials	

    logger.info('Got into the AddMarkInTable method')
    logger.debug(f'table - {table}, cell - {cell}, mark - {mark}')
    try:
        #Ключ API для работы
        CREDENTIALS_FILE = 'GoogleApiKey.json' 

        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) 

        #Id таблицы
        spreadsheetId = '1Hq6BrKSUtFnIV0_rdCaiH36s2NwdIbobTImhJnbeGOE'
          
        rangeTab = str(table) + "!" + str(cell)

        #Сам метод добавления
        #Если пиздец! То лазить тут!
        service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": rangeTab,
                 "majorDimension": "ROWS",     
                 "values": [ [mark] ]
                }
            ]
        }).execute()
        logger.info('The AddMarkInTable method has completed its execution')
    except Exception as ex: 
        logger.exception(ex)

