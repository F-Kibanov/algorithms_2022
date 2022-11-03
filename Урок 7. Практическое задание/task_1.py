"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit

rand_arr = [randint(-100, 101) for i in range(10)]


def bubble_sort(rand_list: list) -> list:
    my_list = rand_list[:]
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


def bubble_sort_optimized(rand_list: list) -> list:
    my_list = rand_list[:]
    count = 0
    flag = True
    while flag:
        flag = False
        for _ in range(len(my_list) - count - 1):
            if my_list[_] < my_list[_ + 1]:
                my_list[_], my_list[_ + 1] = my_list[_ + 1], my_list[_]
                flag = True
        count += 1
    # print(f'Кличество проходов: {count}')
    return my_list


if __name__ == '__main__':
    print(f'Исходный массив:             {rand_arr}')
    print(f'Сортировка пузырьком:        {bubble_sort(rand_arr)}')
    print(f'Оптимизированная сортировка: {bubble_sort_optimized(rand_arr)}')
    # Замеры времени:
    print(f'Время сортировки пузырьком:         {timeit("bubble_sort(rand_arr)", globals=globals(), number=1000)}')
    print(f'Время оптимизированной сортировки:  {timeit("bubble_sort_optimized(rand_arr)", globals=globals(), number=1000)}')

"""
Оптимизация алгоритма сортировки пузырьком позволила сократить время выполнения
на ~30%
"""
