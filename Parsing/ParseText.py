import Parse

def get_link(html):
    """Построчно ищу поля таблицы с id = LC1,LC2 и т.д., затем передаю их на запись в метод csv
    Если больше нет полей таблицы( то есть кода или текстовых данных), тогда метод закончит работу"""
    soup = Parse.BeautifulSoup(html, 'lxml')
    head = soup.find('strong', class_="final-path")
    Parse.csv_read("\nFile Title: "+head.getText()+"\n")
    i = 1
    flag = True
    while flag:
        head = soup.find('td', id="LC"+i.__str__())
        if head is None:
            flag = False
        else:
            Parse.csv_read(head.getText())
            i += 1


url = input("Введите ссылку: ")
Parse.finding_files(Parse.get_html(url), url)