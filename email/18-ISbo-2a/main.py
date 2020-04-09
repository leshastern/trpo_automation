import APIgoogle
import client
import config
import Validation
import log_method

#Временная заглушка
log_method.logger.debug('Program start')
service = APIgoogle.get_service()
message_info = APIgoogle.get_message(service, APIgoogle.user_id)
email = APIgoogle.search_email(message_info['email_id'])
if email is None : 
    APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 3, None, None)
    log_method.logger.debug('Program finished')
    exit()
valid_dict = Validation.validation(message_info['head_of_msg'], message_info['body_of_msg'])
if valid_dict["errorDescription"].count > 0 : 
    APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 2, valid_dict, None)
    log_method.logger.debug('Program finished')
    exit()
answer = client.send_a_laboratory_work_for_verification(labNumber = valid_dict['Number'], labLink = valid_dict['URL'])
if answer["labStatus"] == 0 : 
    APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 1, answer, None)
    log_method.logger.debug('Program finished')
    exit()

data_user = APIgoogle.search_group(email)
cell = APIgoogle.search_tablic(data_user[0], valid_dict['Number'], data_user[1]) 

APIgoogle.add_mark_in_table(data_user[0], cell, 1)
APIgoogle.send_message(service, APIgoogle.user_id, email, APIgoogle.name_surname(message_info['email_id']), 0, None, None)
log_method.logger.debug('Program finished')