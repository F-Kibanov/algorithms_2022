"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from statistics import median
from timeit import timeit


def builtin_median_search(m: int):
    rand_arr = [randint(-100, 101) for _ in range(2 * m + 1)]
    return f'{"-" * 50}\nm = {m}, Медиана = {median(rand_arr)}'


if __name__ == '__main__':
    print(builtin_median_search(10))
    print(f'Время поиска медианы: {timeit("builtin_median_search(10)", globals=globals(), number=10)}')
    print(builtin_median_search(100))
    print(f'Время поиска медианы: {timeit("builtin_median_search(100)", globals=globals(), number=10)}')
    print(builtin_median_search(1000))
    print(f'Время поиска медианы: {timeit("builtin_median_search(1000)", globals=globals(), number=10)}')

"""
Встроенный метод statistics.median оказался на порядок быстрее всех,
что, в общем то, неудивительно
"""