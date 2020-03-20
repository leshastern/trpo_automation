# coding=utf-8


def WorkWithLetters(letters):
    """Работа с письмами, формирование правильного формата данных,
    отправка их на проверку, принятие результатов и их передача дальше"""

    # LettersConvertToString - Вытащить сырые данные и переконвертировать их к строковому в нужном формате
    # convertedLetters - Переменная, хранящая сконвертированные строковые данные
    print("convertedLetters = LettersConvertToString(letters)")

    # FormJSONDates - Сформировать JSON-ы с нужными данными по каждой лабораторной
    # jsonDates - Переменная, хранящая данные в формате JSON
    print("jsonDates = FormJSONDates(convertedLetters)")

    # SendJSONForCheck - Отправить письма на проверку
    print("SendJSONForCheck(jsonDates)")

    # GetResultsFromCheck - Дождаться результатов проверки писем
    # emailResults - Переменная, хранящая результаты проверок
    print("emailResults = GetResultsFromCheck()")

    # SetResults - Передать данные следующему модулю в формате списка экземпляров класса EmailResults
    print("SetResults(emailResults)")

WorkWithLetters("")