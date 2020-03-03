import User
"""Класс LetterResult-результат письма, содержит данные о студенте, при помощи класса User,
Тему письма, является ли решение правильным и Статусы"""


class LetterResult:
    Student = User.User()
    ThemeOfLetter = ""
    IsOK = False
    CodeStatus = 0
    CodeStatusComment = ""

    # Конструктор, все входные данные не обязательны для того, чтобы была возможность сделать пустой экземпляр класса
    def __init__(self, student=None, themeOfLetter=None, isOK=None, codeStatus=None, codeStatusComment=None):
        self.Student = student
        self.ThemeOfLetter = themeOfLetter
        self.IsOK = isOK
        self.CodeStatus = codeStatus
        self.CodeStatusComment = codeStatusComment
