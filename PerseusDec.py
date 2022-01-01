import math
import time


def perseus(func):
    def wrapperfunc():
        starttime = time.time()
        print('Была вызвана функция: {}'.format(func.__name__), '.')
        func()
        endtime = time.time()
        print('Затраченное время выполнения: %s секунды' % (endtime - starttime))
    return wrapperfunc


@perseus
def size():
    print("Расчёт длины и ширины садового участка в акрах.")
    a = float(input("Введите длину участка в футах: = "))
    b = float(input("Введите ширину участка в футах: = "))
    s = a * b
    sqft_per_acre = s/43560
    print("Площадь участка составляет:", round(sqft_per_acre, 2), "акр")


@perseus
def airborne():
    print("Расчёт скорости объекта во время его соприкосновения с землей.\nВведите данные.")
    a = 9.8
    d = int(input("Введите дистанцию для расчёта:"))
    vf = math.sqrt(2 * (a * d))
    print("Скорость тела при соприкосновении с землёй составляет:", vf)


size()
airborne()
