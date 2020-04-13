import log_method


@log_method.log_method_info
def validation(head_of_msg,body_of_msg):
    #Список предметов
    Subjects_list=['ТРПО']
    #Список лабораторных работ
    SubjectNumber_list=['ЛР№1','Лабораторная работа №1','ЛР№2','Лабораторная работа №2',
                        'ЛР№3','Лабораторная работа №3','ЛР№4','Лабораторная работа №4',
                        'ЛР№5','Лабораторная работа №5','ЛР№6','Лабораторная работа №6',
                        'ЛР№7','Лабораторная работа №7','ЛР№8','Лабораторная работа №8',
                        'ЛР№9','Лабораторная работа №9']
    #Список ошибок
    Errors_list=[]
    #Список приветствий
    Greeting_list=['Добрый день','Добрый вечер']
   
    
    
    #Проверка на название предмета
    for x in Subjects_list:
        a=head_of_msg.find(x)
        if a!=-1:
            break
    if a==-1:
        log_method.logger.warning('validation: The name of the item is incorrect.')
        Errors_list.append('неверно указано название предмета')
    
    #Проверка на номер лабораторной
    for x in SubjectNumber_list:
        a=head_of_msg.find(x)
        if a!=-1:
            a=head_of_msg.find('№')
            Number=head_of_msg[a+1]
            break
    if a==-1:
        log_method.logger.warning('validation: The lab number is incorrect.')
        Errors_list.append('неверно указан номер ЛР')
        Number=None
 
    #Проверка на приветствие  
    for x in Greeting_list:
        a=body_of_msg.find(x)
        if a!=-1:
            break
    if a==-1:
        log_method.logger.warning('validation: Missing greeting.')
        Errors_list.append('отсутствует приветствие')

    #Проверка на URL
    URL=url_cheack(Number,body_of_msg)

    #Проверка на подпись
    a=body_of_msg.find('--')
    if a==-1:
        log_method.logger.warning('validation: Missing signature.')
        Errors_list.append('отсутствует подпись')


    #Словарь
    validation_dictionary={ #а я думал кортеж))))
     'Number':Number,
     'URL': URL,
     "errorDescription": Errors_list
    }

    #Возвращаем словарь с номером лабораторной, URL, лист ошибок.
    return(validation_dictionary)
    #print(validation_dictionary)
     
    #Проверка на наличие URL. Возврат ссылки.
@log_method.log_method_info
def url_cheack(Number,body_of_msg):
    #Список ЛР в которых должна содержаться URL
    SubjectNumberURL_list=['7','8','9']
    #Проверка на содержание URL
    for x in SubjectNumberURL_list: #Можно было заменить на if Number in SubjectNumberURL_list:
        if Number==x:
            a=body_of_msg.find('http')
            counter=0
            # Ищем первый пробел после http
            while  a+counter<len(body_of_msg)-1:
                if body_of_msg[a+counter]!=' ':
                    counter= counter+1
                else:
                    break
                #Если дошли до конца не найдя пробелов то...
            if a+counter==len(body_of_msg)-1:
                if body_of_msg[a+counter]=='.':
                    URL=body_of_msg[a:a+counter]
                    return(URL)
                else:
                    URL=body_of_msg[a:a+counter+1]
                    return(URL)
                    break #зачем здесь нужен break? Ведь этот блок не в цикле
                   
            while a+counter>=a:
                if body_of_msg[a+counter]=='.':
                    URL=body_of_msg[a:a+counter]
                    logging.debug('url = %s' % URL)
                    return (URL)                  
                if body_of_msg[a+counter]!='.':
                    counter=counter-1    



#validation("ТРПО.ЛР№2",'Добрый день! Выполнил здание как и просили. Ссылка на репо: https://github.com/MaXL2000/VR_Laboratory.git. -- Лютый Максим 18-ИСбо-2а')
#url_cheack('7', 'https://gi.cm/Sa/tn.git.')

    

