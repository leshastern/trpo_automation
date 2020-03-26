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
import log_method
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from pprint import pprint
import httplib2
import apiclient.discovery
import re;
from oauth2client.service_account import ServiceAccountCredentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.labels', 'https://www.googleapis.com/auth/gmail.modify']

@log_method.log_method_info
def get_service():
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
	return service

service = get_service()
user_id = 'me'

@log_method.log_method_info
def add_mark_in_table(table, cell, mark):
    """
    Добавление отметки в журнал. 
    table - название таблицы. cell - ячейка в таблице. mark - отметка для ячейки.
    """
    import httplib2 
    import apiclient.discovery
    from oauth2client.service_account import ServiceAccountCredentials	

    log_method.logger.debug(f'add_mark_in_table: table - {table}, cell - {cell}, mark - {mark}')
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
        
@log_method.log_method_info
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

@log_method.log_method_info
def name_surname(email):
    """
    Метод для выделения и передачи имени и фамилии.
    """
    comp = re.compile('(\S*?) '+'(\S*?) ')
    y=comp.search(email)
    q=y.group(0)
    return q

@log_method.log_method_info
def search_email(email_id):
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
    result=re.search(email, str(table)) # поиск почты 
    if result != None:
        b=poisk(a)
    else:
        b=None
    return b

def get_message(service, user_id):
	"""
	Метод получения полезной информации из письма студента
	"""
	#Все письма нашей почты с пометкой "INBOX" + их количество
	search_id = service.users().messages().list(userId=user_id, labelIds = ['INBOX']).execute()
	#Выбираем только письма
	message_id = search_id['messages']
	#Берем первое письмо
	alone_msg = message_id[0]
	#Берем его ID
	id_of_msg = alone_msg['id']
	#Дэшифруем наше письмо и получаем всю информацию о нем
	message_list = service.users().messages().get(userId=user_id, id=id_of_msg, format='full').execute()
	#Выбираем только верхние значения с полезной информацией
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
	#Словарь с информацией о Никнейме_и_email_студента, Заголовке и теле письма
	message_info ={
	'email_id':email_id,
	'head_of_msg':head_of_msg,
	'body_of_msg':body_of_msg
	}
	return message_info


@log_method.log_method_info
def send_message(service, user_id, email_of_student, name_of_student, number_of_templates, error_dictionary):
	"""
	Метод по отправке сообщения студенту
	"""

	#Шаблоны писем
	message_templates = [{
		'title':'Работа успешно принята', 'our_msg':'Поздравляю!\nРабота успешно принята!\nОценку можно проверить в журнале:\nhttps://docs.google.com/spreadsheets/d/1gOX8T8ihy3J1khhC16U1qDwaI-K6ndkp9LFWAHncuWA/edit?usp=sharing'},
		{'title':'Обнаружены ошибки в работе', 'our_msg':'В Вашей работе обнаружены ошибки:\n\n' + error_in_work(error_dictionary) + '\nПросьба исправить их и отправить письмо повторно.'},
		{'title':'Обнаружены ошибки в заполнении письма', 'our_msg':'В структуре письма обнаружены следующие ошибки:\n\n' + error_in_work(error_dictionary) + 	'\nПросьба исправить их в соответствии с документом\n' + 'https://docs.google.com/document/d/1DRhgepxVwoscylIS2LCW-po5SFBdqOr-oo92bP_XfHE/edit?usp=sharing'},
		{'title':'Авторизация пользователя', 'our_msg':'Вы не найдены в системе. Пожалуйста, перейдите по ссылке и зарегистрируйтесь.\nhttps://docs.google.com/forms/d/1nXhfOkE3KnWVFNzZ-jvvATAIb6T3zzwD5Ry8Itc-VmQ/edit?usp=sharing'}
		{'title':'Ошибка модулю', 'our_msg':'В модуле ... обнаружена ошибка. В ближайшее время проблема будет исправлена. Просим прощения за неудобства.'
	}]
	sending_msg={}
	#Данные используемые в каждом письме
	hello_student = "Здравствуйте, " + name_of_student + "!\n\n"
	signature = "\n\nС уважением,\nБот"
	sending_msg['from'] = "trpo.automation@gmail.com"
	our_msg = message_templates[number_of_templates]['our_msg']
	title = message_templates[number_of_templates]['title']
	#Определяем тип нашего форматирования
	sending_msg = MIMEMultipart('alternative')
	#Тело нашего сообщения
	sending_msg = MIMEText(hello_student + our_msg + signature)
	#Кому мы его отправляем
	sending_msg['To'] = email_of_student
	#Заголовок нашего сообщения
	sending_msg['Subject'] = title
	#Преобразование строки
	raw = base64.urlsafe_b64encode(sending_msg.as_bytes())
	raw = raw.decode()
	body = {'raw': raw}
	#Отправка
	send_msg = service.users().messages().send(userId=user_id, body=body).execute()

def send_message_to_techsub(service, user_id, email_of_student, name_of_student, error_dictionary, number_of_templates):
	"""
	Метод рассылки писем ТП.
	Вызывается преподавателю, если у студента есть ошибки в работе
	Вызывается, если пал какой-либо модуль
	"""
	message_templates=[{
		'hello':'Здравствуйте, Юрий Викторович!\n\n','title':'Ошибка в работе студента', 'our_msg':'Студент '+name_of_student+' не справился с задачей №'validation_dictionary['Numder']+' ('+validation_dictionary['URL']+')'+
		'\nБыли допущены ошибки в работе:\n\n'+error_in_work(error_dictionary)}
		{'hello':'Здравствуйте!', 'title':'Служба дала сбой', 'our_msg':'В модуле ... возникла ошибка ...'
	}]
	sending_msg={}
	mas_of_To=['yuri.silenok@gmail.com', '0sashasmirnov0@gmail.com', 'k.svyat395@gmail.com', 'MaXLyuT2000@gmail.com', 'majishpro@gmail.com', 'Sirokko77@gmail.com', 'nikita.lukyanow@gmail.com',
	 'generalgrigorevous@gmail.com', 'molchok.yurij@gmail.com', 'amr15319@gmail.com']
	#Данные используемые в каждом письме
	signature = "\n\nС уважением,\nБот"
	sending_msg['From'] = 'trpo.automation@gmail.com'
	#Определяем тип нашего форматирования
	sending_msg = MIMEMultipart('alternative')
	#Тело нашего сообщения
	sending_msg = MIMEText(message_templates[number_of_templates]['hello'] + message_templates[number_of_templates]['our_msg'] + signature)
	#Заголовок нашего сообщения
	sending_msg['Subject'] = message_templates[number_of_templates]['title']
	#Кому мы его отправляем
	if number_of_templates != 0
		#Цикл рассылки сообщений ТП
		for i in mas_of_To:
			sending_msg['To'] = i
			#Преобразование строки
			raw = base64.urlsafe_b64encode(sending_msg.as_bytes())
			raw = raw.decode()
			body = {'raw': raw}
	else
		#Письмо преподавателю в случае ошибок в коде студента
		sending_msg['To'] = 'yuri.silenok@gmail.com'
		#Преобразование строки
		raw = base64.urlsafe_b64encode(sending_msg.as_bytes())
		raw = raw.decode()
		body = {'raw': raw}
	#Отправка
	send_msg = service.users().messages().send(userId=user_id, body=body).execute()

def error_in_work(some_errors):
	"""
	Метод преобразования массива с ошибками в строку
	Метод используется для валидации и ошибок кода студента
	"""
	error = ""
	mas_of_er = some_errors['Errors']
	i=0
	while i<len(mas_of_er):
		error +="- "+mas_of_er[i]+"\n"
		i+=1
	return error
