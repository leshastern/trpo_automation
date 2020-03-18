#coding: utf-8
from config import SPREAD_SHEET_ID
from config import CREDENTIALS_FILE
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import email
import base64
import logging
import logging.config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from pprint import pprint
import httplib2
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.labels', 'https://www.googleapis.com/auth/gmail.modify']

logging.config.fileConfig('logging_config.conf')
logger = logging.getLogger(__name__)

def get_service():
	logger.info('Got into the get_service method')
	creds = None
	 # The file token.pickle stores the user's access and refresh tokens, and is
	 # created automatically when the authorization flow completes for the first
	 # time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('gmail', 'v1', credentials=creds)
	print(service)
	logger.debug(f'service - {service}')
	logger.info('The get_service method has completed its execution')
	return service

service = get_service()
user_id = 'me'


#def error_in_work #Ожидает выполнение работы метода Валидации 



def send_message(service, user_id, email_of_student, name_of_student, our_msg, title):
	logger.info('Got into the send_message method')
	sending_msg={}
	#Данные используемые в каждом письме
	hello_student = "Здравствуйте," + name_of_student + "\n\n"
	signature = "\n\nС уважением,\n Бот"
	sending_msg['from'] = "trpo.automation@gmail.com"

	sending_msg = MIMEMultipart('alternative')
	#Тело нашего сообщения
	sending_msg = MIMEText(hello_student + our_msg + signature)
	#Кому мы его отправляем
	sending_msg['to'] = email_of_student
	#Заголовок нашего сообщения
	sending_msg['subject'] = title
	#Преобразование строки
	raw = base64.urlsafe_b64encode(sending_msg.as_bytes())
	raw = raw.decode()
	body = {'raw': raw}
	#Отправка
	send_msg = service.users().messages().send(userId=user_id, body=body).execute()
	logger.info('The server_otvet method has completed its execution')



def add_mark_in_table(table, cell, mark):
    """
    Добавление отметки в журнал. 
    table - название таблицы. cell - ячейка в таблице. mark - отметка для ячейки.
    """
    import httplib2 
    import apiclient.discovery
    from oauth2client.service_account import ServiceAccountCredentials	

    logger.info('Got into the AddMarkInTable method')
    logger.debug(f'table - {table}, cell - {cell}, mark - {mark}')
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) 
          
        rangeTab = str(table) + "!" + str(cell)

        #Сам метод добавления
        #Если пиздец! То лазить тут!
        service.spreadsheets().values().batchUpdate(spreadsheetId = SPREAD_SHEET_ID, body = {
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
def name_surname(email):
    """
    Метод для выделения и передачи имени и фамилии.
    """
    comp = re.compile('(\S*?) '+'(\S*?) ')
    y=comp.search(email)
    q=y.group(0)
    return q
def search_email(email):
    """
    Метод для поиска в таблице.
    email - передаваемая строка с почтой
    """
    a=email
    #email=cleaning_email(email) # вызываю метод очистки строки в нужный формат
    CREDENTIALS_FILE = 'json файл'  #  ← имя скаченного файла с закрытым ключом
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',                                                                               'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
    spreadsheetId = 'ссылка на таблицу'
    range_name = 'Лист1!B1:B1000'
    table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute() 
    result=re.search(email, str(table)) # поиск почты 
    if result != None:
        b=poisk(a)
    else:
        b=None
    return b



def programm_progress(service, user_id):
	logger.info('Got into the programm_progress method')
	try:
		search_id = service.users().messages().list(userId=user_id, labelIds = ['INBOX']).execute()
		#список наших собщений в папке "Входящие"
		message_id = search_id['messages']
		logger.debug(f'message_id - {message_id}')
		#количество наших сообщений в папке
		number_results = search_id['resultSizeEstimate']
		logger.debug(f'number_results - {number_results}')

		while search_id['resultSizeEstimate'] > 0:
			alone_msg = message_id[0]
			id_of_msg = alone_msg['id']
			message_list = service.users().messages().get(userId=user_id, id=id_of_msg, format='full').execute()
			
			#Часть сообщения верхнего уровня с полезной информацией
			info_of_msg = message_list.get('payload')['headers']

			email_id = '' # Имя и ГуглМаил отправителя
			head_of_msg = '' # Тема письма
			body_of_msg = '' # Тело письма

			for head in info_of_msg :
				if head['name'] == 'From' :
					email_id = head['value']
				if head['name'] == 'Subject' :
					head_of_msg = head['value']
			body_of_msg = message_list['snippet']


			#Разбиваем нашу строку email_id на email и name_of_student
			name_of_student = name_surname(email_id)
			email_of_student = cleaning_email(email_id)


			if #метод авторизации отработал и нашел человека
				#отправляем письмо с фразами, что работа принята к рассмотрению
				if #метод Макса отработал и студент правильно запомнил 
					if #метод обработки самой лабораторной работы
						#если словарь ошибок пуст, то высылаем письмо о завершении проверки
						title = "Работа успешно принята"
						our_msg = "Поздравляю!\nРабота успешно принята!\nОценку можно проверить в журнале:\n" + "https://docs.google.com/spreadsheets/d/1gOX8T8ihy3J1khhC16U1qDwaI-K6ndkp9LFWAHncuWA/edit?usp=sharing"
						send_message(service, user_id, email_of_student, name_of_student, our_msg, title)


					else #у студента есть ошибки в работе
						title = "Обнаружены ошибки в работе"
						our_msg = "В Вашей работе обнаружены ошибки:\n" + error_in_work + "Просьба исправить их и отправить письмо повторно"
						send_message(service, user_id, email_of_student, name_of_student, our_msg, title)
				else #если сообщение заполнено неверно, то высылается
				title = "Обнаружены ошибки в заполнении письма"
				our_msg = "В структуре письма обнаружены следующие ошибки:\n" + error_in_msg() + 
				"\nПросьба исправить их в соответствии с документом\n" + "https://docs.google.com/document/d/1DRhgepxVwoscylIS2LCW-po5SFBdqOr-oo92bP_XfHE/edit?usp=sharing" 	
				send_message(service, user_id, email_of_student, name_of_student, our_msg, title)
					

			else #метод не нашел человека
				title = "Авторизация пользователя"
				our_msg = "Вы не найдены в системе. Пожалуйста, перейдите по ссылке и зарегистрируйтесь.\n" + "https://docs.google.com/forms/d/1nXhfOkE3KnWVFNzZ-jvvATAIb6T3zzwD5Ry8Itc-VmQ/edit?usp=sharing"
				send_message(service, user_id, email_of_student, name_of_student, our_msg, title)
			#архивация сообщения(403 недостаточно прав для gmail api с python)
			label_id = 'id_of_msg' 
			# ID of user label to add
			filter = {
				'criteria': {
					'from': 'email_id'
				},
				'action': {
					'addLabelIds': [label_id],
					'removeLabelIds': ['INBOX']
				}
				}
			result = service.users().settings().filters().create(userId=user_id, body=filter).execute()
			logger.info('Created filter: %s' % result.get('id'))			
	except (errors.HttpError. error):
		logger.exception(("An error occured: %s") % error)
	except Exception as ex:
		logger.exception(ex)
	finally:
		logger.info('The programm_progress method has completed its execution')
		return messages
