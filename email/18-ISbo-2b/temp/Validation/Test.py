from mail.Google.Validation import ValidateLetters, Letter, User

u = User.User('a', 'b', 'c', True)

t1 = 'ТРПО ЛР3 ВАР2'
t2 = 'ТРПО ЛР12 ВАР 2'
t3 = 'ТРПО ЛР 10 ВАРИАНТ 9'
t4 = 'ТРПО ЛР20 ВАР0'
t5 = 'ТРПО ЛР ВАР2'

b = """
Здравствуйте
https://github.com/
Ельцов Андрей, 18-ИСбо-2б"""

let1 = Letter.Letter(u)
let2 = Letter.Letter(u)
let3 = Letter.Letter(u)
let4 = Letter.Letter(u)
let5 = Letter.Letter(u)

let1.ThemeOfLetter = t1
let2.ThemeOfLetter = t2
let3.ThemeOfLetter = t3
let4.ThemeOfLetter = t4
let5.ThemeOfLetter = t5

let1.Body = b
let2.Body = b
let3.Body = b
let4.Body = b
let5.Body = b

letters = []
letters.append(let1)
letters.append(let2)
letters.append(let3)
letters.append(let4)
letters.append(let5)

ValidateLetters.ValidateLetters(letters)
