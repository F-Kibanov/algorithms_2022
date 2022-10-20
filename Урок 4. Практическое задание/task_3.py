"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from random import randint
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


"""
Наилучший результат показала функция revers_3, использующая срез строки 
с шагом -1. На втором месте - функция revers_4, которая сначала переводит
строчную переменную enter_num в список, потом применяет к нему встроенный
метод reverse(), и в конце присоединяет перевернутый список к пустой строке
при помощи .join(). Такие результаты можно объяснить использованием встроенных
методов, у которых неплохое быстродействие "из коробки", а также отсутствием
рекурсии, как в функции revers_1 и цикла while в revers_2, которые замедляют
рааботу программы.
"""


def revers_4(enter_num):
    num_list = list(str(enter_num))
    num_list.reverse()
    reverse_num = "".join(num_list)
    return reverse_num


if __name__ == '__main__':
    num = randint(1_000_000, 1_000_000_000)
    print(timeit('revers(num)', globals=globals(), number=1000))
    print(timeit('revers_2(num)', globals=globals(), number=1000))
    print(timeit('revers_3(num)', globals=globals(), number=1000))
    print(timeit('revers_4(num)', globals=globals(), number=1000))

