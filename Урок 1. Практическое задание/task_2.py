"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib_cached(n):
    cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
    return result


"""
В процессе рекурсивного выполнения функции одни и те же объекты 
высчитываются по многу раз, что порождает излишнее потребление памяти
и процессорного времени. Самый простой метод избавиться от этих потерь - 
воспользоватьсся механизмом кеширования, чтоб запоминать уже посчитанные
значения и не тратить память и время на их повторное вычисление.
"""


if __name__ == '__main__':
    print(fib(35))
    print(fib_cached(35))
