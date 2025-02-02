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

Это файл для пятого скрипта
"""
from recordclass import recordclass as rc
from memory_profiler import profile

"""
В домашних заданиях больше не нашел функций, которые можно оптимизировать,
поэтому решил использовать стороннюю задачу для проверки модуля recordclass.
Заполните словарь n-парами ключ-значение, где ключ - порядковый номер начиная 
с 1, а значение - его квадрат.
"""


@profile
def dict_fill(n):
    my_dict = {}
    for i in range(1, n + 1):
        my_dict.setdefault(i, i ** 2)
    return  # my_dict


@profile
def dict_fill_optimized(n):
    my_list = []
    my_rc = rc('my_recordclass', 'i i2')
    for i in range(1, n + 1):
        my_list.append(my_rc(i, i**2))
    return  # my_list


if __name__ == '__main__':
    print(dict_fill(100000))
    print(dict_fill_optimized(100000))


"""
Это явно не лучшее применение recordclass, но было интересно попробовать его 
в деле, да и экономия памяти все равно присутствует на больших выборках. 
Вот вывод консоли для n=100_000:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     29.0 MiB     29.0 MiB           1   @profile
    45                                         def dict_fill(n):
    46     29.0 MiB      0.0 MiB           1       my_dict = {}
    47     40.4 MiB      5.9 MiB      100001       for i in range(1, n + 1):
    48     40.4 MiB      5.5 MiB      100000           my_dict.setdefault(i, i ** 2)
    49     40.4 MiB      0.0 MiB           1       return  # my_dict


None

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    52     29.7 MiB     29.7 MiB           1   @profile
    53                                         def dict_fill_optimized(n):
    54     29.7 MiB      0.0 MiB           1       my_list = []
    55     29.7 MiB      0.0 MiB           1       my_rc = rc('my_recordclass', 'i i2')
    56     38.9 MiB      9.3 MiB      100001       for i in range(1, n + 1):
    57     38.9 MiB      0.0 MiB      100000           my_list.append(my_rc(i, i**2))
    58                                         
    59     38.9 MiB      0.0 MiB           1       return  # my_list


None

Process finished with exit code 0
"""