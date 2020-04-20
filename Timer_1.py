from time import *
import time
import threading

global start_time


def func():
    sleep(3)
    for i in range(3):
        print('Алгоитм продолжает работу...')
        sleep(1.5)


def SetTimer():
    """
    Записывает в глобальную переменную текущее значение времени
    :return:
    """
    global start_time
    start_time = int(time.time())


def WaitTimer():
    """
    Когда выполнение кода доходит до конца модуля, вызывается эта функция
    Сравнивает текущее значение времени с записанным в глобальную переменную и ждет, если разность не превышает
    заданного интервала. Ожидание через sleep потока. При этом для продолжения работы программы создается дополнительный
    поток
    :return:
    """
    now_time = int(time.time())
    next_work = threading.Thread(target=func)
    next_work.start()
    while now_time - start_time < 10:
        sleep(2)
        now_time = int(time.time())
        print(f"wait... осталось {10 - (now_time - start_time)} секунд")
    print('new iteration')


SetTimer()
WaitTimer()
