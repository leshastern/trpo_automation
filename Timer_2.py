from threading import Timer

global i
i = 1


def CheckEmail():
    """
    Первая функция цикла проверки лабораторных работ. При ее вызове отрабатывает весь алгоритм
    Должна включать в себя вызов функции SetTimer()
    :return:
    """
    global i
    SetTimer()
    print(i, 'iteration')
    i = i + 1


def SetTimer():
    """
    Реализация через класс threading.Timer. Запускает первую функцию цикла раз в определнный промежуток времени
    (первый параметр в строке создания объекта. В сеундах)
    В этом случае таймер можно остановить до его начала вызовом t.cancel()
    :return:
    """
    t = Timer(2, CheckEmail)
    t.start()


SetTimer()
