"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def without_sort(m: int):
    rand_arr = [randint(-100, 101) for _ in range(2 * m + 1)]
    for _ in range(m):
        rand_arr.remove(max(rand_arr))
    return f'{"-" * 50}\nm = {m}, Медиана = {max(rand_arr)}'


if __name__ == '__main__':
    print(without_sort(10))
    print(f'Время поиска медианы: {timeit("without_sort(10)", globals=globals(), number=10)}')
    print(without_sort(100))
    print(f'Время поиска медианы: {timeit("without_sort(100)", globals=globals(), number=10)}')
    print(without_sort(1000))
    print(f'Время поиска медианы: {timeit("without_sort(1000)", globals=globals(), number=10)}')

"""
Поиск медианы без предварительной сортировки происходит значительно быстрее,
особенно если у сортировки была сложность O(n**2)
"""
