import re
import json


def validation_subject(subject):
    subject = subject.lower()
    if subject[0:4] != "трпо":
        return "subject_exception"
    index = subject.find("лр", 0, 10)
    number_work = subject[index + 2:index + 5]
    if number_work[0].isdigit() and number_work[1].isdigit():
        return number_work[0:2]
    elif number_work[0].isdigit():
        return number_work[0]
    else:
        number_work = number_work[1:3]
    if number_work[0].isdigit() and number_work[1].isdigit():
        return number_work
    elif number_work[1].isdigit():
        return number_work[1]
    else:
        return "subject_exception"


def validation_body(body):
    links = []
    strings = body.split('\n')
    for item in strings:
        if item == "" or item == "--":
            strings.remove(item)
    if len(strings) < 3:
        return "body_exception"
    name = strings[len(strings) - 1]
    name = re.split(' ', name)
    name[1] = name[1].replace(',', '')  # Удалил запятую
    FirstName = name[0]
    LastName = name[1]
    Group = name[2]
    for item in strings:
        pattern = re.findall(r'https://[^ ]*', item)  # [^ ]*
        if len(pattern) != 0:
            links.append(pattern)
    if len(links) == 0:
        return "links_exception"
    return FirstName, LastName, Group, links


def validation(subject, body):
    try:
        NumberWork = validation_subject(subject)
        FirstName, LastName, Group, Links = validation_body(body)
        data = [FirstName, LastName, Group, NumberWork, Links]
        filename = "student_information.txt"
        file = open(filename, mode='w', encoding='utf-8')
        json.dump(data, file, ensure_ascii=False)
        file.close()
    except ChildProcessError:
        if NumberWork.isdigit():
            return "validation_body_error"
        else:
            return "validation_subject_error"


ex0 = "ТРПО ЛР08 название"
ex1 = """Здравствуйте

Исправил работу. Прошу проверить. 
Спасибо
https://www.draw.io/#G1u2wTwjbTJHQQe1qTiWlYytpz_a8huL9I  https://tproger.ru/translations/regular-expression-python/
--
Андрей Ельцов, 18-ИСбо-2б"""


validation(ex0, ex1)
