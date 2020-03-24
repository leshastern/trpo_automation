# coding=utf-8
import User


class LetterResult:
    """Класс LetterResult-результат письма, содержит данные:
    Студент-Student, при помощи класса User,
    Тема письма-ThemeOfLetter
    Является ли решение правильным-IsOK
    Вариант лабораторной работы - Variant
    Статусы-CodeStatus, CodeStatusComment"""
    Student = User.User()
    ThemeOfLetter = ""
    IsOK = False
    Comment = ""
    Variant = 0
    CodeStatus = 0
    CodeStatusComment = ""

    def __init__(self, student=None, themeOfLetter=None, isOK=None, variant=None):
        """Конструктор, все входные данные не обязательны для того,
         чтобы была возможность сделать пустой экземпляр класса"""
        self.Student = student
        self.ThemeOfLetter = themeOfLetter
	self.IsOK = isOK
        self.Variant = variant
