import APIgoogle
import client
import config
import Validation
import log_method

#Временная заглушка
log_method.logger.debug('Program start')
dummy ={"errorDescription": [0]}
service = APIgoogle.get_service()
message_info = APIgoogle.get_message(service, APIgoogle.user_id)
email = APIgoogle.search_email(message_info['email_id'])
if email is None : 
    APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 3, dummy)
    log_method.logger.debug('Program finished')
    exit()
valid_dict = Validation.validation(message_info['head_of_msg'], message_info['body_of_msg'])
if valid_dict["errorDescription"].count > 0 : 
    APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 2, valid_dict)
    log_method.logger.debug('Program finished')
    exit()
answer = client.send_a_laboratory_work_for_verification(labNumber = valid_dict['Number'], labLink = valid_dict['URL'])
if answer["labStatus"] == 0 : 
    APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 1, answer)
    log_method.logger.debug('Program finished')
    exit()

#Нет метода поиска ячейки

APIgoogle.add_mark_in_table('18-ИСбо-2а', 'G7', 1)
APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 0, dummy)
log_method.logger.debug('Program finished')