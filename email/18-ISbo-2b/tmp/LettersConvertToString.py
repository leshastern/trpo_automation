# coding=utf-8
import global_User as User
import global_Letter as Letter
import requests
from bs4 import BeautifulSoup


def LettersConvertToString(letters):
    """Предположительно пока что забираем ссылки из писем на репозиторий"""
    for tmp in letters:
        html = get_html(tmp.Body)
        tmp.Body = finding_files(html, tmp.Student.NameOfStudent)
    return letters



def get_html(url):
    """Достаю html с введённой ссылки и возвращаю в виде текста"""
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text


def csv_read(data):
    """Принятые данные принимает, проверяя: являются ли они строковыми данными
    Если да, записываю их в файл, в конце делаю перенос строки"""
    if isinstance(data, str):
        with open("data.txt", 'a') as file:
            file.write(data+'\n')
            return data


def get_link(html):
    """Построчно ищу поля таблицы с id = LC1,LC2 и т.д., затем передаю их на запись в метод csv
    Если больше нет полей таблицы( то есть кода или текстовых данных), тогда метод закончит работу"""
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('strong', class_="final-path")
    data = ""
    if head != None:
        csv_read("\nFile Title: "+head.getText()+"\n")
    i = 1
    flag = True
    while flag:
        head = soup.find('td', id="LC"+i.__str__())
        if head is None:
            flag = False
        else:
            data += csv_read(head.getText())
            i += 1
    return data


def finding_files(html, name):
    """Метод отвечает за поиск и открытие файлов или папок в репозитории Git'a;
    если ссылка, которую мы открыли не имеет ссылок на другие объекты(файлы или папки),
    мы предполагаем, что это открытый файл и передаём его на парсинг файла в get_link"""
    main_data = ""
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('td', class_ = "content")
    date = finding_links(table)
    if len(date) == 0:
        data = get_link(html)
        return data
    for item in date:
        title = item.get('title')
        if title == name or title.split(".")[0] == name:
            item = item.get('href')
            if item != None:
                main_data += finding_files(get_html("https://github.com"+item), name)
    return main_data



def finding_links(table):
    """Ищет ссылки, на которые можно перейти, то есть проверяет есть ли файлы или папки
    на этой странице или же это уже страница самого файла"""
    date = []
    for item in table:
        date.append(item.find('a', class_="js-navigation-open"))
        if date[len(date) - 1] == None:
            date = date[:len(date) - 1]
    return date


student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)
student1 = User.User("СантьягоЦеместес", "18-ИСбо-2", None, None)
letters = []
letter = Letter.Letter(student, "ЛР01", "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР01", None)
letter1 = Letter.Letter(student1, "ЛР02", "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР02", None)
letters.append(letter)
letters.append(letter1)
LettersConvertToString(letters)