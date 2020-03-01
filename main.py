import re
import json


def validation_subject(subject):  # Проверяю шаблон ТРПО, ЛР и номер лабы
    subject = subject.lower()
    if subject[0:4] != "трпо":  # Проверка на абр. ТРПО
        return False
    index = subject.find("лр", 0, 10)
    if index == -1:  # Проверка абр. ЛР
        return False
    number_work = subject[index + 2:index + 5]
    if (number_work[0].isdigit() and number_work[1].isdigit()) or number_work[0].isdigit():
        return True
    else:
        number_work = number_work[1:3]
    if (number_work[0].isdigit() and number_work[1].isdigit()) or number_work[1].isdigit():
        return True
    else:
        return False


def validation_body(body):  # Проверяю приветствие, ссылки и подпись
    salutation = ["здравствуйте", "добрый", "привет"]  # Шаблоны приветствия
    links = []
    strings = body.split('\n')
    for item in strings:  # Убираю все лишнее
        if item == "" or item == "--":
            strings.remove(item)
    if len(strings) < 3:
        return False
    hello = re.match(r'\w+', strings[0])  # Проверка приветствия по шаблону
    hello = hello.group(0)
    if hello in salutation is None:
        return False
    name = strings[len(strings) - 1]  # Это подпись
    res = re.match(r'\w+[ ]?\w+[, ]{2}\d{2}[-]?\w{4}[-]?\d\w', name)  # Проверяю подпись
    if res is None:
        return False
    for item in strings:  # Проверяю ссылки
        pattern = re.findall(r'https://[^ ]*', item)
        if len(pattern) != 0:
            links.append(pattern)
    if len(links) == 0:  # Если ссылок нет, то False
        return False
    return True


def validation(subject, body):
    if validation_subject(subject) is True and validation_body(body) is True:
        return True
    return False


ex0 = "ТРПО ЛР08 название"
ex1 = """Здравствуйте

Исправил работу. Прошу проверить. 
Спасибо
https://www.draw.io/#G1u2wTwjbTJHQQe1qTiWlYytpz_a8huL9I  https://tproger.ru/translations/regular-expression-python/
--
Андрей Ельцов, 18-ИСбо-2б"""


print(validation(ex0, ex1))


# subject = subject.lower()
#     if subject[0:4] != "трпо":  # Проверка на абр. ТРПО
#         return false
#     index = subject.find("лр", 0, 10)  # Поиск абр. ЛР
#     number_work = subject[index + 2:index + 5]
#     if number_work[0].isdigit() and number_work[1].isdigit():
#         return number_work[0:2]
#     elif number_work[0].isdigit():
#         return number_work[0]
#     else:
#         number_work = number_work[1:3]
#     if number_work[0].isdigit() and number_work[1].isdigit():
#         return number_work
#     elif number_work[1].isdigit():
#         return number_work[1]
#     else:
#         return false


# links = []
#     strings = body.split('\n')
#     for item in strings:
#         if item == "" or item == "--":
#             strings.remove(item)
#     if len(strings) < 3:
#         return "body_exception"
#     name = strings[len(strings) - 1]
#     name = re.split(' ', name)
#     name[1] = name[1].replace(',', '')  # Удалил запятую
#     FirstName = name[0]
#     LastName = name[1]
#     Group = name[2]
#     for item in strings:
#         pattern = re.findall(r'https://[^ ]*', item)  # [^ ]*
#         if len(pattern) != 0:
#             links.append(pattern)
#     if len(links) == 0:
#         return "links_exception"
#     return FirstName, LastName, Group, links
