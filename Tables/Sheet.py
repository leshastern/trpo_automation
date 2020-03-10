"""
Подключение класса, вызов метода проверки наличия студента в базе.
Метод принимает строковые параметры (обязательные),
проверяет наличие email в базе, в случае отсутствия - добавляет
информацию о студенте последней строкой.
Ничего не возвращает!
"""

#Просто скопируйте это в вашу программу:

"""
from Sheet import Sheet

email = 'test@gmail.com'    #замените здесь на ваши данные
group = 'группа'    #замените здесь на ваши данные
first_name = 'имя'  #замените здесь на ваши данные
surname = 'фамилия' #замените здесь на ваши данные
patronymic = 'отчество' #замените здесь на ваши данные

Sheet.check_student_email(email, group, first_name, surname, patronymic)
"""

from Auth import Auth
import datetime
import re

class Sheet:

    #пока так)))
    def __init__(self):
        #Авторизация в сервисе
        self.service = Auth.auth_sheets()
        
        #ID документа в гугл-таблицах
        self.spreadsheetId = '1gMZiZqSE89vk3ZeYbTGYGaMMy7j-iMrYRjn-ECUhaag'

    #получение названия листа
    def sheet_name():
        service = Sheet().service
        spreadsheetId = Sheet().spreadsheetId
        
        # Получаем список листов, их Id и название
        spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
        sheetList = spreadsheet.get('sheets')
        for sheet in sheetList:
            #sheet['properties']['sheetId'] # если понадобится id_листа
            sheet['properties']['title']
    
        sheet_name = sheetList[0]['properties']['title']
        return sheet_name    

    
    """
    #чтение листа
    Если указан только sheet_name(имя листа) - возвращает весь лист

    если дополнительно указан второй необязательный параметр,
    то возвращается содержимое запрошенной ячейки, т.е.
    diapazon_start - это адрес ячейки с которой начинается чтение, например,
    diapazon_start = "B2"

    * если дополнительно указан третий необязательный параметр,
    то возвращается содержимое запрошенного диапазона.
    diapazon_end - это конечный адрес выбираемого диапазона.
    Может иметь формат адреса ячейки, например, "D4".
    ** Или может являться просто названием столбца - "D",
    тогда будет возвращен все содержимое столбца,
    начиная с запрошенной начальной ячейки
    
    * Конечный диапазон должен быть больше начального

    ** Это будет работать только в случае, если вы указываете
    в конечный диапазон тот же столбец, что и в начальном диапазоне,
    иначе третий параметр не будет обработан!
    """
    #чтение листа
    def read_sheet(sheet_name, diapazon_start = "", diapazon_end = ""):
        service = Sheet().service
        spreadsheetId = Sheet().spreadsheetId
        null_ptr = ""
        
        if diapazon_start != null_ptr:
            if diapazon_end != null_ptr:
                ranges_str = sheet_name + "!" + diapazon_start + ":" + diapazon_end
            else: ranges_str = sheet_name + "!" + diapazon_start
        else: ranges_str = sheet_name

        ranges = [ranges_str]

        #ranges = ["Ответы на форму (1)!B2:B"] #Формат диапазона для запроса
                  
        results = service.spreadsheets().values().batchGet(spreadsheetId = spreadsheetId, 
                                             ranges = ranges, 
                                             valueRenderOption = 'FORMATTED_VALUE',  
                                             dateTimeRenderOption = 'FORMATTED_STRING').execute() 
        sheet_values = results['valueRanges'][0]['values']
        return sheet_values

    #Запись в конец листа, принимает строковый диапазон, и объект
    def append_sheet(ranges, body):
        service = Sheet().service
        spreadsheet_id = Sheet().spreadsheetId
        range_ = ranges
        value_input_option = 'USER_ENTERED'
        insert_data_option = 'INSERT_ROWS'
        value_range_body = body

        request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()

    #Добавление записи в конец листа
    #принимает набор обязательных параметров, ничего не возвращает!
    def new_student(email, group, first_name, surname, patronymic):
        today = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
        
        ranges = 'Ответы на форму (1)'
        
        body = {
            "range": "Ответы на форму (1)", #диапазон 
            "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы#         "values": [
            "values": [
                        [today, email, surname, first_name, patronymic, group] # Заполняем строку
                    ]
            }
        
        Sheet.append_sheet(ranges, body) #Добавление записи в конец листа

    #проверка наличия студента в базе, в случае отсутствия - добавление, ничего не возвращает
    def check_student_email(email, group, first_name, surname, patronymic):
        sheet_name = Sheet.sheet_name() #имя листа

        d_start = "B2"  #начало диапазона
        d_end = "B" #конец диапазона
        
        #получаем все email из списка
        email_full = Sheet.read_sheet(sheet_name, d_start, d_end)

        #проверка наличия email в списке
        email_str = ' '.join(map(str, email_full))
        
        pattern = "\[\'" + email + "\'\]"        
        match = re.search(pattern, email_str)
        if not match:
            Sheet.new_student(email, group, first_name, surname, patronymic)
            #print("добавлено")
        #else:
        #    print("Уже существует")
        #    print(match[0])
        
