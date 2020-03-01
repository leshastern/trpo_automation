class User:
    NameOfStudent = ""
    GroupOfStudent = ""
    Email = ""
    IsRegistered = False

    def __init__(self, name=None, group=None, mail=None, registered=None):
        self.NameOfStudent = name
        self.GroupOfStudent = group
        self.Email = mail
        self.IsRegistered = registered
