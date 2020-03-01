import User


class LetterResult:
    Student = User.User()
    ThemeOfLetter = ""
    IsOK = False
    CodeStatus = 0
    CodeStatusComment = ""

    def __init__(self, student=None, themeOfLetter=None, isOK=None, codeStatus=None, codeStatusComment=None):
        self.Student = student
        self.ThemeOfLetter = themeOfLetter
        self.IsOK = isOK
        self.CodeStatus = codeStatus
        self.CodeStatusComment = codeStatusComment
