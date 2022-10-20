"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """
    Испольование list comprehensions и отказ от .append помогло уменьшить
    время работы функции в ~1.5 раза.
    """

    return [i for i in range(len(nums)) if not nums[i] % 2]


if __name__ == '__main__':
    nums = list(range(1000))
    print(timeit('func_1(nums)', globals=globals(), number=1000))
    print(timeit('func_2(nums)', globals=globals(), number=1000))
