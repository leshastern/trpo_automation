from mail.Google.Validation.main import ValidationMail as Val
import re


def ValidateLetters(letters):
    for let in letters:
        if let.CodeStatus is None:
            val = Val(let.ThemeOfLetter, let.Body)
            let.CodeStatus = val.validation(val.subject, val.body)
            if let.CodeStatus == '02':
                let.CodeStatusComment = 'Структура письма не соответствует требованиям к оформлению'
            elif let.CodeStatus == '03':
                let.CodeStatusComment = 'Номер варианта меньше 1 или больше 15 или не число'
            else:
                num, var = val.get_num_and_var(val.subject)
                if int(num) < 1 or int(num) > 15 or int(var) == 0:
                    let.CodeStatus = '03'
                    let.CodeStatusComment = 'Номер лабораторной не существует'
                else:
                    let.Number = var
                    let.Variant = num
            if let.CodeStatus == '20':
                let.Body = re.findall(r'http[^ \n]*', let.Body)
                let.CodeStatusComment = 'Работа отправлена на проверку'
