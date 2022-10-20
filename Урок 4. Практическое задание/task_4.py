"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


"""
Самое простое решение - использовать функцию Counter из встроенного модуля
collections. При этом такое решение оказывается самым медленным, так как
метод most_common каждый раз возвращает список кортежей, в которых содержатся 
элемент массива и количество его вхождений.
"""


def func_3():
    return Counter(array).most_common(1)[0][0]


if __name__ == '__main__':
    print(timeit('func_1()', globals=globals(), number=1000))
    print(timeit('func_2()', globals=globals(), number=1000))
    print(timeit('func_3()', globals=globals(), number=1000))
