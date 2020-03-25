import APIgoogle
import client
import config
import Validation

service = APIgoogle.get_service()
message_info = APIgoogle.get_message(service, APIgoogle.user_id)
email = APIgoogle.search_email(message_info['email_id'])
if email == None : 
    #Вставить сюда отправку с ошибкой
    exit()
valid_dict = Validation.validation(message_info['head_of_msg'], message_info['body_of_msg'])
if valid_dict['Errors'].count > 0 : 
    # Вставить отправку с ошибкой
    exit()
answer = client.send_a_laboratory_work_for_verification(labNumber = valid_dict['Number'], labLink = valid_dict['URL'])
if answer == 0 : 
    #Вставить отправку с ошибкой
    exit()

#Нет метода поиска ячейки

APIgoogle.add_mark_in_table('18-ИСбо-2а', 'G7', answer)

#Вставить отправку