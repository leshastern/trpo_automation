import User
"""Класс Letter-письмо, содержит данные о студенте, при помощи класса User,
Тему письма, его содержание и Статусы"""


class Letter:
    Student = User.User() #Экземпляр класса User
    ThemeOfLetter = "" #Тема письма
    Body = object() #Содержание письма
    CodeStatus = 0
    CodeStatusComment = ""

    # Конструктор, все входные данные не обязательны для того, чтобы была возможность сделать пустой экземпляр класса
    def __init__(self, student=None, themeOfLetter=None, body=None, codeStatus=None, codeStatusComment=None):
        self.Student = student
        self.ThemeOfLetter = themeOfLetter
        self.Body = body
        self.CodeStatus = codeStatus
        self.CodeStatusComment = codeStatusComment
