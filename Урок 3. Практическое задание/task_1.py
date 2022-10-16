"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import time


def time_measure(function):  # O(1)
    def wrapped():
        start_time = time.time()
        res = function()
        return f'Время выполнения функции: {time.time() - start_time}, Результат: {res}'

    return wrapped


my_list = []
my_dict = {}


# a)
@time_measure
def list_fill(n=100_000):  # O(N)
    for i in range(n):  # O(N)
        my_list.append(i)  # O(1)
    return 'my_list filled!'


@time_measure
def dict_fill(n=100_000):  # O(N)
    for k in range(n):  # O(N)
        my_dict.setdefault(k, k)  # O(1)
    return 'my_dict filled!'


"""
Список заполняется быстрее, потому что, в отличие от словаря,
для списка не надо вычислять значение хеш-функции для каждого
элемента.
"""


# b)
@time_measure
def get_list_items(l=my_list):  # O(N)
    item = [i for i in l]  # O(N)
    return 'my_list extracted!'


@time_measure
def get_dict_keys(d=my_dict):  # O(N)
    for k in d.keys():  # O(N)
        value = k
    return 'my_dict keys extracted!'


@time_measure
def get_dict_values(d=my_dict):  # O(N)
    for v in d.values():  # O(N)
        value = v
    return 'my_dict values extracted!'


@time_measure
def get_dict_items(d=my_dict):  # O(N)
    for key, value in d.items():  # O(2*N) == O(N)
        k, v = key, value
    return 'my_dict extracted!'


"""
Извлечение ключей и значений из словаря по отдельности занимает
время, сравнимое с временем извлечения элементов списка, при этом 
одновременное извлечение пары "ключ - значение" занимает в ~2 раза
больше времени, чем извлечение значений из списка, что может объясняться
в два раза большим объемом работы, которую необходимо проделать.
"""


# c)
@time_measure
def drop_list_forward(l=my_list):  # O(N**2)
    while l:  # O(N)
        first_item = l.pop(0)  # O(N)
    return 'my_list_forward dropped!'


@time_measure
def drop_list_reverse(l=my_list):  # O(N)
    while l:  # O(N)
        last_item = l.pop()  # O(1)
    return 'my_list_reverse dropped!'


@time_measure
def drop_dict(d=my_dict):  # O(N)
    for item in range(len(d)):  # O(N)
        item = d.pop(item)  # O(1)
    return 'my_dict dropped!'


""""
Удаление элементов из списка в обратном порядке происходит приблизительно
в два раза быстрее удаления элементов из словаря, что так же может объясняться
в два раза большим количеством элементов в словаре (на один элемент списка
приходится пара "ключ-значение" словаря); при этом удаление элементов списка в 
прямом порядке занимает гораздо больше времени, что объясняется необходимостью
перестроения списка при каждой операции .pop(0).
"""

if __name__ == '__main__':
    print(list_fill())
    print(dict_fill())
    print(get_list_items())
    print(get_dict_keys())
    print(get_dict_values())
    print(get_dict_items())
    print(drop_list_forward())
    list_fill()
    print(drop_list_reverse())
    print(drop_dict())
