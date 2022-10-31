"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""
from memory_profiler import profile
from numpy import array

"""
Задание №1_2 из курса 'Основы языка Python'
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 
(куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело 
на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 
6 + 8 + 5 + 9 = 28 – делится нацело на 7.
"""


# Оригинальное решение
@profile
def sum_list_1(dataset: list) -> int:
    print("# Оригинальное решение")
    dataset = []
    for i in range(1, 1000, 2):
        dataset.append(i ** 3)
    sum_a = 0
    check_a = 0
    for number_a in dataset:
        count_a = 0
        check_a = number_a
        while check_a > 0:
            count_a += check_a % 10
            check_a = check_a // 10
        if count_a % 7 == 0:
            sum_a += number_a
    return sum_a


# Оптимизированное решение
@profile
def sum_list_1_optimized(dataset: array):
    print("# Оптимизированное решение")

    def wrapped():
        summ = 0
        for n in dataset:
            summ += n if not sum([int(n) for n in str(n)]) % 7 else 0
        yield summ

    return wrapped()


if __name__ == '__main__':
    print(sum_list_1(1000))
    print(*sum_list_1_optimized(array([i ** 3 for i in range(1, 1000, 2)])))

"""
Применение генераторной функции не принесло особого эффекта, зато использование
numpy.ndarray привело к заметной экономии памяти при увеличении исходного
списка до 100_000 элементов.

Вывод консоли:

# Оригинальное решение

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    48     43.0 MiB     43.0 MiB           1   @profile
    49                                         def sum_list_1(dataset: list) -> int:
    50     43.0 MiB      0.0 MiB           1       print("# Оригинальное решение")
    51     43.0 MiB      0.0 MiB           1       dataset = []
    52     45.3 MiB      0.5 MiB       50001       for i in range(1, 100000, 2):
    53     45.3 MiB      1.8 MiB       50000           dataset.append(i ** 3)
    54     45.3 MiB      0.0 MiB           1       sum_a = 0
    55     45.3 MiB      0.0 MiB           1       check_a = 0
    56     45.3 MiB      0.0 MiB       50001       for number_a in dataset:
    57     45.3 MiB      0.0 MiB       50000           count_a = 0
    58     45.3 MiB      0.0 MiB       50000           check_a = number_a
    59     45.3 MiB      0.0 MiB      756690           while check_a > 0:
    60     45.3 MiB      0.0 MiB      706690               count_a += check_a % 10
    61     45.3 MiB      0.0 MiB      706690               check_a = check_a // 10
    62     45.3 MiB      0.0 MiB       50000           if count_a % 7 == 0:
    63     45.3 MiB      0.0 MiB        5858               sum_a += number_a
    64     45.3 MiB      0.0 MiB           1       return sum_a


1409831608061185538

# Оптимизированное решение

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     44.6 MiB     44.6 MiB           1   @profile
    69                                         def sum_list_1_optimized(dataset: array):
    70     44.6 MiB      0.0 MiB           1       print("# Оптимизированное решение")
    71                                         
    72     44.6 MiB      0.0 MiB           1       def wrapped():
    73                                                 summ = 0
    74                                                 for n in dataset:
    75                                                     summ += n if not sum([int(n) for n in str(n)]) % 7 else 0
    76                                                 yield summ
    77                                         
    78     44.6 MiB      0.0 MiB           1       return wrapped()


1409831608061185538

Process finished with exit code 0
"""
