import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import email
import base64

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_message(service, user_id, msg_id):

	try:
		search_id = service.users().messages().list(userId=user_id, labelIds = ['INBOX']).execute()
		#список наших собщений в папке "Входящие"
		message_id = search_id['messages']
		#количество наших сообщений в папке
		number_results = search_id['resultSizeEstimate']

		iter=0
		email_stack = []
		while search_id['resultSizeEstimate']>0
			alone_msg = message_id[0]
			id_of_msg = alone_msg['id']
			message_list = service.users().messages().get(userId=user_id, id=id_of_msg, format='raw').execute()
			msg_raw = base64.urlsafe_b64decode(message_list['raw'].encode('ASCII'))
			msg_str = email.message_from_bytes(msg_raw)
			email_id = msg_str.get_all('From')
			email_stack[iter] = email_id

			#уточнить дальнейшие действия с найденным майлом

			if #метод Никиты отработал и нашел человека
				#отправляем письмо с фразами, что работа принята к рассмотрению
				#включаются остальные методы
			else #метод не нашел человека
				#включаем метод Макса(валидация)



			#архивация сообщения(Разобраться)
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
			result = gmail_service.users().settings().filters().create(userId=user_id, body=filter).execute()
			print 'Created filter: %s' % result.get('id')			







	except (errors.HttpError. error):
		print("An error occured: %s") % error:
	return messages



def search_messages(service, user_id, search_string):

	try:
		search_id = service.users().messages().list(userId=user_id, q=search_string).execute()
		message_id = search_id['messages']


		number_results = search_id['resultSizeEstimate']

		final_list = []
		if number_results>0:
			massages_ids = search_id['messages']

			for ids in massages_ids:
				final_list.append(ids['id'])

			return final_list
		else:
			print('There were 0 results fot that string, returing an empty string')
			return ""

	except (errors.HttpError. error):
		print("An error occured: %s") % error:


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
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    return service