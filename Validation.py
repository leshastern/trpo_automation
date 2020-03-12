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
    if a==-1:Errors_list.append('Неерно указано название предмета')
    
    #Прповерка на номер лабораторной
    for x in SubjectNumber_list:
        a=head_of_msg.find(x)
        if a!=-1:
            a=head_of_msg.find('№')
            Number=head_of_msg[a+1]
            break
    if a==-1:
        Errors_list.append('Неверно указан номер ЛР')
        Number=None
 
    #Проверка на приветсвие  
    for x in Greeting_list:
        a=body_of_msg.find(x)
        if a!=-1:
            break
    if a==-1:Errors_list.append('Отсутсвует приветсвие')

    #Проверка на URL
    URL=url_cheack(Number,body_of_msg)

    #Проверка на подпись
    a=body_of_msg.find('--')
    if a==-1:Errors_list.append('Отсутсвует подпись')


    #Словарь
    validation_dictionary={
     'Number':Number,
     'URL': URL,
     'Errors': Errors_list
    }

    #Возвращаем словарь с номером лабораторной,URL,лист ошибок.
    return(validation_dictionary)
    #print(validation_dictionary)
     
    #Проверка на наличие URL.Возврат ссылки.
def url_cheack(Number,body_of_msg):
    #Список ЛР в которых должна содержаться URL
    SubjectNumberURL_list=['7','8','9']
    #Прповерка на содержание URL
    for x in SubjectNumberURL_list:
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
                    print(URL)
                    return(URL)
                else:
                    URL=body_of_msg[a:a+counter+1]
                    print(URL)
                    return(URL)
                    break 
                   
            while a+counter>=a:
                if body_of_msg[a+counter]=='.':
                    URL=body_of_msg[a:a+counter]
                    print(URL)
                    return (URL)                  
                if body_of_msg[a+counter]!='.':
                    counter=counter-1    



#validation("ТРПО.ЛР№2",'Добрый день! Выполнил здание как и просили. Ссылка на репо: https://github.com/MaXL2000/VR_Laboratory.git. -- Лютый Максим 18-ИСбо-2а')
#url_cheack('7', 'https://gi.cm/Sa/tn.git.')

    

