
def Validation(head_of_msg,body_of_msg):
    Subjects_list=[' ТРПО','ТРПО.',' ТРПО.']
    SubjectNumber_list=[' ЛР№1','.ЛР№1',' Лабораторная работа №1','.Лабораторная работа №2']
    
    
    #Проверка на название предмета
    for x in Subjects_list:
        a=head_of_msg.find(x)
        if a!=-1:
            Error='Нет ошибок'
            break
    if a==-1:Error='Неверно указано название предмета'
    
    #Прповерка на номер лабораторной
    for x in SubjectNumber_list:
        a=head_of_msg.find(x)
        if a!=-1:
            a=head_of_msg.find('№')
            Number=head_of_msg[a+1]
            break
    if a==-1:Number='Неверно указан номер ЛР'
    
    #Словарь
    r={
    'Number':Number,
     'URL': "",
     'Errors': Error
    }
    
    b=URL_cheack(Number,body_of_msg)
    print(r,b)
        
def URL_cheack(Number,body_of_msg):
    SubjectNumberURL_list=['7','8','9']
    #Прповерка на содержание URL
    for x in SubjectNumberURL_list:
        if Number==x:
            a=body_of_msg.find('http')
            counter=1

            while body_of_msg[a+counter]!=' ' and a+counter<len(body_of_msg)-1:
                counter= counter+1
            URL=body_of_msg[a:a+counter]
    return URL

Validation("ТРПО. ЛР№1",'Переделал ранее созданный собственный репозиторий. Ссылка на репозиторий: https://github.com/MaXL2000/VR_Laboratory.git')
#URL_cheack('7', 'sad sadas httpsadsa' )

    
