"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

my_list = []
my_deque = deque()


# 1. Сравниваем быстродействие операций append, pop, extend
def list_append_test(n):
    for i in range(n):
        my_list.append(n)
    return my_list


def deque_append_test(n):
    for i in range(n):
        my_deque.append(n)
    return my_deque


def list_pop_test(n):
    for i in range(n):
        my_list.pop()
    return my_list


def deque_pop_test(n):
    for i in range(n):
        my_deque.pop()
    return my_list


def list_extend_test(n):
    for i in range(n):
        my_list.extend([i for i in range(10)])
    return my_list


def deque_extend_test(n):
    for i in range(n):
        my_deque.extend([i for i in range(10)])
    return my_list


"""
Быстродействие list и deque в опреациях append, pop и extend
примерно одинаковое.
"""


# 2. Сравниваем быстродействие операций appendleft, popleft, extendleft
def list_appendleft_test(n):
    for i in range(n):
        my_list.insert(0, n)
    return my_list


def deque_appendleft_test(n):
    for i in range(n):
        my_deque.appendleft(n)
    return my_deque


def list_popleft_test(n):
    for i in range(n):
        my_list.pop(0)
    return my_list


def deque_popleft_test(n):
    for i in range(n):
        my_deque.popleft()
    return my_list


def list_extendleft_test(n):
    for i in range(n):
        my_list.insert(0, [i for i in range(10)])
    return my_list


def deque_extendleft_test(n):
    for i in range(n):
        my_deque.extendleft([i for i in range(10)])
    return my_list


"""
Быстродействие deque в операциях вставки с левого края массива
на порядки выше, чеи у list.
"""


# 3. Сравниваем операции получения элемента по индексу в list и deque.
def list_getitem_test(n):
    for i in range(n):
        my_list[i] = i
    return my_list


def deque_getitem_test(n):
    for i in range(n):
        my_deque[i] = i
    return my_deque


"""
Быстродействие list в опреациях взятия элемента по индексу немного 
лучше, чем у deque.
"""


if __name__ == '__main__':
    print('list append: ', (timeit('list_append_test(1000)', globals=globals(), number=100)))
    print('deque append: ', timeit('deque_append_test(1000)', globals=globals(), number=100))
    print('list pop: ', timeit('list_pop_test(1000)', globals=globals(), number=100))
    print('deque pop: ', timeit('deque_pop_test(1000)', globals=globals(), number=100))
    print('list extend: ', timeit('list_extend_test(1000)', globals=globals(), number=100))
    print('deque extend: ', timeit('deque_extend_test(1000)', globals=globals(), number=100))
    print('list "appendleft": ', (timeit('list_appendleft_test(1000)', globals=globals(), number=10)))
    print('deque appendleft: ', timeit('deque_appendleft_test(1000)', globals=globals(), number=10))
    print('list "popleft": ', timeit('list_popleft_test(1000)', globals=globals(), number=10))
    print('deque popleft: ', timeit('deque_popleft_test(1000)', globals=globals(), number=10))
    print('list "extendleft": ', timeit('list_extendleft_test(1000)', globals=globals(), number=10))
    print('deque extendleft: ', timeit('deque_extendleft_test(1000)', globals=globals(), number=10))
    print('list get item: ', timeit('list_getitem_test(1000)', globals=globals(), number=10000))
    print('deque get item: ', timeit('deque_getitem_test(1000)', globals=globals(), number=10000))

