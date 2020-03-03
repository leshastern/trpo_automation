# coding=utf-8
class AnswersForUsers:
    """класс AnswersForUsers-ответы пользователям, содержит данные:
    Кому написано-Who
    Что написано-What"""
    Who = ""
    What = ""

    def __init__(self, who=None, what=None):
        """Конструктор, все входные данные не обязательны для того,
                 чтобы была возможность сделать пустой экземпляр класса"""
        self.Who = who
        self.What = what
