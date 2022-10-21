"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ordered_dict = OrderedDict()


def fill_dict(n):
    for i in range(n):
        my_dict[i] = i
    return my_dict


def fill_ordered_dict(n):
    for i in range(n):
        my_ordered_dict[i] = i
    return my_ordered_dict


def get_dict_val(n):
    for i in range(n):
        j = my_dict[i]
    return my_dict


def get_ordered_dict_val(n):
    for i in range(n):
        j = my_ordered_dict[i]
    return my_ordered_dict


def set_dict_val(n):
    for i in range(n):
        my_dict[i] = i ** 2
    return my_dict


def set_ordered_dict_val(n):
    for i in range(n):
        my_ordered_dict[i] = i ** 2
    return my_ordered_dict


def drop_dict_val(n):
    for i in range(n):
        for key in my_dict.keys():
            my_copy = my_dict.copy()
            del my_copy[key]


def drop_ordered_dict_val(n):
    for i in range(n):
        for key in my_ordered_dict.keys():
            my_ordered_copy = my_ordered_dict.copy()
            del my_ordered_copy[key]


"""
Операции заполнения, чтения и замены значений в обычном словаре и упорядоченном 
словаре происходят примерно с одинаковой скоростью, но операция удаления 
элементов в упорядоченном словаре занимает существенно больше времени.
Применение OrderedDict может быть оправданно в случаях, когда требуются
его специфичные функции, такие как move_to_end или popitem, а так же 
когда требуется явно показать, что в этом словаре порядок элеметов важен
для корректной работы программы, и нет необходимости в частом удалении элементов.
"""

if __name__ == '__main__':
    print('fill dict:             ', timeit('fill_dict(1000)', globals=globals(), number=1000))
    print('fill ordered dict:     ', timeit('fill_ordered_dict(1000)', globals=globals(), number=1000))
    print('get dict val:          ', timeit('get_dict_val(1000)', globals=globals(), number=1000))
    print('get ordered dict val:  ', timeit('get_ordered_dict_val(1000)', globals=globals(), number=1000))
    print('set dict val:          ', timeit('set_dict_val(1000)', globals=globals(), number=1000))
    print('set ordered dict val:  ', timeit('set_ordered_dict_val(1000)', globals=globals(), number=1000))
    print('drop dict val:         ', timeit('drop_dict_val(10)', globals=globals(), number=10))
    print('drop ordered dict val: ', timeit('drop_ordered_dict_val(10)', globals=globals(), number=10))
