"""класс User - пользователь, студент, имеющий основные данные:
 ФИ студента, его группа, email и является ли он зарегистрированным
"""


class User:
    NameOfStudent = "" #ФИ студента
    GroupOfStudent = "" #Группа студента
    Email = "" #email студента
    IsRegistered = False #Является ли зарегистрированным

    #Конструктор, все входные данные не обязательны для того, чтобы была возможность сделать пустой экземпляр класса
    def __init__(self, name=None, group=None, mail=None, registered=None):
        self.NameOfStudent = name
        self.GroupOfStudent = group
        self.Email = mail
        self.IsRegistered = registered
