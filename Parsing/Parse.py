import requests
from bs4 import BeautifulSoup


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


def get_link(html):
    """Построчно ищу поля таблицы с id = LC1,LC2 и т.д., затем передаю их на запись в метод csv
    Если больше нет полей таблицы( то есть кода или текстовых данных), тогда метод закончит работу"""
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('strong', class_="final-path")
    csv_read("\nFile Title: "+head.getText()+"\n")
    i = 1
    flag = True
    while flag:
        head = soup.find('td', id="LC"+i.__str__())
        if head is None:
            flag = False
        else:
            csv_read(head.getText())
            i += 1


def finding_files(html, url):
    """Метод отвечает за поиск и открытие файлов или папок в репозитории Git'a;
    если ссылка, которую мы открыли не имеет ссылок на другие объекты(файлы или папки),
    мы предполагаем, что это открытый файл и передаём его на парсинг файла в get_link"""
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('td', class_ = "content")
    date = finding_links(table)
    if len(date) == 0:
        get_link(html)
    for item in date:
        item = item.get('href')
        last = str(item).split("/")
        if last[len(last)-1] != None:
            finding_files(get_html(url+"/"+last[len(last)-1]), url+"/"+last[len(last)-1])
    return


def finding_links(table):
    """Ищет ссылки, на которые можно перейти, то есть проверяет есть ли файлы или папки
    на этой странице или же это уже страница самого файла"""
    date = []
    for item in table:
        date.append(item.find('a', class_="js-navigation-open"))
        if date[len(date) - 1] == None:
            date = date[:len(date) - 1]
    return date


url = input("Введите ссылку: ")
finding_files(get_html(url), url)

