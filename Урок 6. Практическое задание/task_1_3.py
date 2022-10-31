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

Это файл для третьего скрипта
"""
from memory_profiler import profile

"""
Задание №3 из курса 'Знакомство с языком Python'
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
"""


# Оригинальное решение
@profile
def fib_list(n: int):
    print("# Оригинальное решение")
    list_fibs = [0, 1]
    f1 = 0
    f2 = 1
    i = 0
    while i <= n:
        f1, f2 = f2, f2 + f1
        i += 1
        list_fibs.append(f2)
    return "\n"  # list_fibs


# Оптимизированное решение
@profile
def fib_list_optimized(n: int):
    print("# Оптимизированное решение")

    def wrapped():
        fib1, fib2 = 0, 1
        for i in range(n):
            fib1, fib2 = fib2, fib1 + fib2
            yield fib1
    return wrapped()  # tuple(wrapped())


if __name__ == '__main__':
    print(fib_list(100000))
    print(fib_list_optimized(100000))

"""
Использование генераторной функции вместо классического цикла while
позволяет достичь тем большей экономии памяти, чем больший ряд Фибоначчи
требуется вычислить. При малых значениях n потребление памяти у обеих функций
одинаковое, но с увеличеним значения n потребление памяти значительно растет 
в первой функции и остается практически неизменным во второй, так как она 
возвращает не список, а объект генератор. Конечно, если преобразовать объект 
генератора в список, потребление памяти станет одинаковым за счет размеров 
самого списка, но при возврате объекта генератор функция выполняется очень 
быстро и занимет одно и то же количество памяти. Пробовал использовать кортеж 
вместо списка во второй функции, но по замерам получилось даже чуть большее 
потребление памяти, чем в списке.


Вывод консоли:

# Оригинальное решение

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    41     28.9 MiB     28.9 MiB           1   @profile
    42                                         def fib_list(n: int):
    43     28.9 MiB      0.0 MiB           1       print("# Оригинальное решение")
    44     28.9 MiB      0.0 MiB           1       list_fibs = [0, 1]
    45     28.9 MiB      0.0 MiB           1       f1 = 0
    46     28.9 MiB      0.0 MiB           1       f2 = 1
    47     28.9 MiB      0.0 MiB           1       i = 0
    48    475.0 MiB      0.0 MiB      100002       while i <= n:
    49    475.0 MiB    443.2 MiB      100001           f1, f2 = f2, f2 + f1
    50    475.0 MiB      0.0 MiB      100001           i += 1
    51    475.0 MiB      3.0 MiB      100001           list_fibs.append(f2)
    52    475.0 MiB      0.0 MiB           1       return "\n"  # list_fibs




# Оптимизированное решение

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    55     33.5 MiB     33.5 MiB           1   @profile
    56                                         def fib_list_optimized(n: int):
    57     33.5 MiB      0.0 MiB           1       print("# Оптимизированное решение")
    58                                         
    59     33.5 MiB      0.0 MiB           1       def wrapped():
    60                                                 fib1, fib2 = 0, 1
    61                                                 for i in range(n):
    62                                                     fib1, fib2 = fib2, fib1 + fib2
    63                                                     yield fib1
    64     33.5 MiB      0.0 MiB           1       return wrapped()  # tuple(wrapped())


<generator object fib_list_optimized.<locals>.wrapped at 0x7f20c828f6d0>

Process finished with exit code 0
"""
