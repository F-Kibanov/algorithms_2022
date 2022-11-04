"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def gnome_sort(m: int):
    rand_arr = [randint(-100, 101) for _ in range(2 * m + 1)]
    index = 1
    i = 0
    n = len(rand_arr)
    while i < n - 1:
        if rand_arr[i] <= rand_arr[i + 1]:
            i, index = index, index + 1
        else:
            rand_arr[i], rand_arr[i + 1] = rand_arr[i + 1], rand_arr[i]
            i -= 1
            if i < 0:
                i, index = index, index + 1
    return f'{"-" * 50}\nm = {m}, Медиана = {rand_arr[m]}\nОтсортированный массив: {rand_arr}'


if __name__ == '__main__':
    print(gnome_sort(10))
    print(f'Время сортировки: {timeit("gnome_sort(10)", globals=globals(), number=10)}')
    print(gnome_sort(100))
    print(f'Время сортировки: {timeit("gnome_sort(100)", globals=globals(), number=10)}')
    print(gnome_sort(1000))
    print(f'Время сортировки: {timeit("gnome_sort(1000)", globals=globals(), number=10)}')

"""
Гномья сортировка неплохо работает на небольших списках, но с ростом количества
элементов время сортировки увеличивается в квадратичной зависимости
"""
