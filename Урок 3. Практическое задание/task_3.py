"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib

set_hashes = set()


def uniq_sustrs(my_str):
    for n in range(len(my_str) - 1):
        m = 0
        n += 1
        while n <= len(my_str):
            str_slice = my_str[m: n]
            hashed_slice = hashlib.sha256(str_slice.encode('utf-8')).hexdigest()
            set_hashes.add(hashed_slice)
            m += 1
            n += 1
    return set_hashes


if __name__ == '__main__':
    my_set = uniq_sustrs('papa')
    for el in my_set:
        print(el)
