import User


class Letter:
    Student = User.User()
    ThemeOfLetter = ""
    Body = object()
    CodeStatus = 0
    CodeStatusComment = ""

    def __init__(self, student=None, themeOfLetter=None, body=None, codeStatus=None, codeStatusComment=None):
        self.Student = student
        self.ThemeOfLetter = themeOfLetter
        self.Body = body
        self.CodeStatus = codeStatus
        self.CodeStatusComment = codeStatusComment
